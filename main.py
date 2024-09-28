#importing log objects from src folder
from src.DiseaseClassifier import logger
#importing the ingestion pipeline 
from src.DiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME="Data Ingestion Stage"
if __name__=='__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        ingest=DataIngestionTrainingPipeline()
        ingest.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e