import os
import cv2
import numpy as np

from label_decoder import LabelDecoder

import torch
import torch.nn as nn

import albumentations as A
from albumentations.pytorch import ToTensorV2

from efficient_net import EfficientNet

from torch.utils.data import Dataset
from torch.utils.data.sampler import SequentialSampler

from flask import Flask, request, render_template, send_from_directory, make_response,jsonify

class Prediction:
    def __init__(self):

        self.model_0 = self.load_model("model/224_b0_0.pt")
        #self.model_1 = self.load_model("model/224_b0_1.pt")
        #self.model_2 = self.load_model("model/224_b0_2.pt")
        #self.model_3 = self.load_model("model/224_b0_3.pt")
        #self.model_4 = self.load_model("model/224_b0_4.pt")
        
        print("Model Loaded")

    def Net(self, model_name = 'b0', output = 14):
        model = EfficientNet.from_pretrained(f'efficientnet-{model_name}')
        model._fc = nn.Linear(in_features = model._fc.in_features, out_features = output, bias = True)
        return model

    def load_model(self, path):
        model = self.Net().to(torch.device('cpu'), dtype=torch.float32)
        model.load_state_dict(torch.load(path, map_location=torch.device('cpu'))["model_state_dict"])
        model.eval()
        return model


    def validation_augmentations(self, img_size = 224):
        return A.Compose([
                A.Resize(height=img_size, width=img_size, p=1.0),
                ToTensorV2(p=1.0),
            ], p=1.0)

    class DatasetRetriever(Dataset):

        def __init__(self, image_ids, transforms=None):
            super().__init__()
            self.image_ids = image_ids

            self.transforms = transforms

        def __getitem__(self, idx: int):
            image_id = self.image_ids[idx]
            image = cv2.imread(image_id, cv2.IMREAD_COLOR)

            if self.transforms:
                sample = {'image': image}
                sample = self.transforms(**sample)
                image = sample['image']

            return image

        def __len__(self) -> int:
            return self.image_ids.shape[0]


    def predict(self, path):
        test_dataset = self.DatasetRetriever(np.array([path]), self.validation_augmentations(img_size = 224))  
        test_loader = torch.utils.data.DataLoader(
                    test_dataset,
                    batch_size=1,
                    num_workers=1,
                    shuffle=False,
                    sampler=SequentialSampler(test_dataset),
                    pin_memory=False,
                )


        for _, x_test in enumerate(test_loader):
            images = x_test.to(torch.device('cpu'), dtype=torch.float32)
            
            #final_pred=(self.model_0(images) + self.model_1(images) + self.model_2(images) + 
                        #self.model_3(images) + self.model_4(images)) / 5
            print("Prediction started")
            final_pred=(self.model_0(images))
            print("Prediction ended")
            y_pred = nn.functional.softmax(final_pred, dim=1).data.cpu().numpy().argmax()


            #topk_values = torch.topk(y_pred, 3).values.data.cpu().numpy()[0] 
            #topk_indices = torch.topk(y_pred, 3).indices.data.cpu().numpy()[0]
            
            return LabelDecoder(y_pred)

app = Flask(__name__)


#UPLOAD_FOLDER = "/home/rahul/Workspace/pulses-classification/static"
@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":

        image_file = request.files["image"]

        if image_file:      
            basepath = os.path.dirname(__file__)
            img_path = os.path.join(basepath, 'static', image_file.filename)

            image_file.save(img_path)
            pred = Prediction().predict(img_path)
            print(image_file.filename)
            return render_template("index.html", prediction=pred, image_loc=image_file.filename)
    return render_template("index.html", prediction=0, image_loc=None)

if __name__ == "__main__":

    app.run(debug=True)

    