#importing log objects from src folder
from src.DiseaseClassifier import logger
#importing the ingestion pipeline 
from src.DiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.DiseaseClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline


#In this file we call all the pipeline functions
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
    


STAGE_NAME="Prepare Base Model"
if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=PrepareBaseModelPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e