import json

def LabelDecoder(key):
    
    with open('req_files/label_key.json') as f:
        KEY = json.load(f)

    INV_KEY = {v: k for k, v in KEY.items()}

    return INV_KEY[key]
