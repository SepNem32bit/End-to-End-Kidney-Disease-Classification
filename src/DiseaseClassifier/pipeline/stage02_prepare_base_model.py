from src.DiseaseClassifier.config.config_manager import ConfigurationManager
from src.DiseaseClassifier.components.prepare_base_model_components import PrepareBaseModel
from src.DiseaseClassifier import logger


STAGE_NAME="Prepare Base Model"

class PrepareBaseModelPipeline():

    def main(self):
        config= ConfigurationManager()
        
        prepare_base_model_config=config.get_prepare_base_ml_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        


if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=PrepareBaseModelPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e