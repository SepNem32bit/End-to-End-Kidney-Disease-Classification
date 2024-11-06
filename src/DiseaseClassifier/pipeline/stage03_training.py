from src.DiseaseClassifier.config.config_manager import ConfigurationManager
from src.DiseaseClassifier.components.model_training_components import Training
from src.DiseaseClassifier import logger


STAGE_NAME="MODEL TRAINING"
class TrainingPipeline():
    def main(self):
        config= ConfigurationManager()
        training_config=config.get_training_ML_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=TrainingPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e