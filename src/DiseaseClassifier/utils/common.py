#All common codes are written here
import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
#Because the file was defined in setup so no need for src.DiseaseClassifier
from DiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64



#The @ensure_annotations decorator in Python is typically used to enforce that the function adheres to its type annotations at runtime. It ensures that:
# The inputs to the function match the types specified in the function signature.
# The output of the function matches the return type annotation.
#A decorator in Python is a design pattern that allows you to modify the behavior of a function or class without changing its code.
#for example in this function inputs and outputs are integer. If we input any other data type, it'll give us an error
# get_multiplications(x=3,y="2")
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
#ConfigBox enables us to call values of keys in dic ,this way: dic.key
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {Path}")


@ensure_annotations
#This function saves json file which will be used for the model metrics
#path to json file
#data to be saved in json file (dict)
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at:{Path}")


@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    with open(path) as f:
        content=json.load(f)
    
    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

#Base64 is an encoding scheme used to convert binary data into a string format made up of ASCII characters. 
#It is commonly used to encode data that needs to be safely transmitted over media designed to handle textual data, such as email or JSON. 
#This encoding ensures that binary data (like images, files, etc.) doesn't get corrupted when passed through systems that only accept text.

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())


def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"wb") as f:
        f.write(imgdata)

