#importing log objects from src folder
from src.DiseaseClassifier import logger
#importing the pipelines
from src.DiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.DiseaseClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from src.DiseaseClassifier.pipeline.stage03_training import TrainingPipeline
from src.DiseaseClassifier.pipeline.stage04_mlflow_evaluation import EvaluationPipeline


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
    



STAGE_NAME="MODEL TRAINING"
if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=TrainingPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e
    

###To be reviewed###

STAGE_NAME="MLFLOW EVALUATION"
if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=EvaluationPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e