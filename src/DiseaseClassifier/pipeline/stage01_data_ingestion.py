from src.DiseaseClassifier.config.config_manager import ConfigurationManager
from src.DiseaseClassifier.components.data_ingestion import DataIngestion
#logger be found in init file
from DiseaseClassifier import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline():

    def main(self):
        try:
            config= ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            #I can't download my file from the google drive so I saved it locally and moved it to artifacts file
            # data_ingestion.download_file()
            # data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
    
if __name__=='__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        ingest=DataIngestionTrainingPipeline()
        ingest.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e

