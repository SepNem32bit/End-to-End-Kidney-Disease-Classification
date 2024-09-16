import os
from pathlib import Path
import logging

#Logging Strung
#It's useful to see all results intead of using print
#ASCI format time
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name='DiseaseClassifier'

list_files=[
    #we want a dummy file in an empty folder to let us commit our folder
    '.github/workflows/.gitkeep',
    #we will have all of the components of our projects in src (source) folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    #for web flask implementation
    "templates/index.html"
]


for filePath in list_files:
    #converting the path to the current operating system
    filePath=Path(filePath)
    #separating directory and file name
    filedir,filename=os.path.split(filePath)


    if filedir!="":
        #creating directory
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file: {filename}")
<<<<<<< HEAD
    #if the path exist or the file doesn't contain any code so it won't affect those with codes
=======
    #if the path exist or the file doesn't contain any code
>>>>>>> 9683f9418798614453b2f4a13c80804ea2454c6c
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filePath}")

    else:
        logging.info(f"{filename} is already exists")