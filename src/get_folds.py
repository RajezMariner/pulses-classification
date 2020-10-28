import json
import numpy as np
import pandas as pd

from sklearn import preprocessing 
from sklearn import model_selection

df = pd.read_csv(r'/home/rahul/Workspace/Maa ji for Bachelor/functionalities/Pulse Classification/req_files/dataset.csv')

''' K - Fold validation '''

K = 5 # 5 Folds

df = df.sample(frac=1).reset_index(drop=True)

kf = model_selection.StratifiedKFold(n_splits=K)

df["k-fold"] = -1

for fold, (tra_, val_) in enumerate(kf.split(X = df, y = df.Label.values)):
  df.loc[val_,"k-fold"] = fold
  print(f'Fold No : {fold}, Training label count : {len(tra_)}, Validation label count : {len(val_)}')

''' Label Encoding '''

label_encoder = preprocessing.LabelEncoder() 

label_encoder.fit(df['Label'])

KEY = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))

df['Label_enc']= label_encoder.transform(df['Label'])
  
df['Label_enc'].unique()

# Handle int64 files
class npEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int64):
            return int(obj)
        return json.JSONEncoder.default(self, obj)
        
with open(r'/home/rahul/Workspace/Maa ji for Bachelor/functionalities/Pulse Classification/req_files/label_key.json', 'w') as f:
    json.dump(KEY, f, cls=npEncoder) # Dumping Label_Key to be refered later
    print('Label Key dumped')

df.to_csv(r'/home/rahul/Workspace/Maa ji for Bachelor/functionalities/Pulse Classification/req_files/dataset_folds.csv', index=False)