from src.DiseaseClassifier.constants import *
from src.DiseaseClassifier.utils.common import read_yaml, create_directories
from src.DiseaseClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseMLConfig

#retreiving all ingestion config parameters
    
class ConfigurationManager:
    def __init__(self,
                 #from constants
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        #init file for referencing the config files
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        #we have artifacts_root in config file
        #It'll go through directories and create artifacts folder and subfolders
        create_directories([self.config.artifacts_root])
    #we've defined DataIngestionConfig class above
    def get_data_ingestion_config(self)->DataIngestionConfig:
        #data_ingestion in artifacts, config file 
        config=self.config.data_ingestion
        #referring to data_ingestion, artifacts, config file
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    



    #This method creates the directory structure needed for the base machine learning configuration 
    #and returns an instance of PrepareBaseMLConfig
    #we've defined DataIngestionConfig class above
    def get_prepare_base_ml_config(self)->PrepareBaseMLConfig:
        #prepare_base_ML in artifacts, config file 
        config=self.config.prepare_base_ML
        #referring to prepare_base_ML, artifacts, config file
        create_directories([config.root_dir])

        prepare_base_ml_config=PrepareBaseMLConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            )
        return prepare_base_ml_config
