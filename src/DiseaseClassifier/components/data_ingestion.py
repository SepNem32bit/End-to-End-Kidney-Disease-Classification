import gdown
import zipfile
import os
from src.DiseaseClassifier import logger
from src.DiseaseClassifier.utils.common import get_size
from src.DiseaseClassifier.entity.config_entity import DataIngestionConfig


#downloading and unzipping files when it's needed

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self)->str:
        try:
            dataset_url=self.config.source_file
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifcats/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id=dataset_url.split('/')[-2]
            prefix="https://drive.google.com/uc?export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        #locating the zip file
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            #extract it into unzip_path
            zip_ref.extractall(unzip_path)