import os
import glob
import csv
import pandas as pd 

BASE_LOCATION = r'/home/rahul/Workspace/Maa ji for Bachelor/functionalities/Pulse Classification/dataset'

TEMP_PATH = list()
TEMP_LABEL = list()

for each_label in os.listdir(BASE_LOCATION):

    path = glob.glob(os.path.join(BASE_LOCATION, each_label +r'/*jpg'))
    label = [each_label] * len(path)

    TEMP_PATH.extend(path)
    TEMP_LABEL.extend(label)

df = pd.DataFrame(list(zip(TEMP_PATH, TEMP_LABEL)), columns =['Path', 'Label'])

df.to_csv(r'/home/rahul/Workspace/Maa ji for Bachelor/functionalities/Pulse Classification/req_files/dataset.csv', index=False)