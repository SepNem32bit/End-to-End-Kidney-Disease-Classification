from src.DiseaseClassifier.config.config_manager import ConfigurationManager
from src.DiseaseClassifier.components.mlflow_model_evaluation_components import Evaluation
from src.DiseaseClassifier import logger


###To be reviewed###

STAGE_NAME="MLFLOW EVALUATION"
class EvaluationPipeline():
    def main(self):
        config= ConfigurationManager()
        evaluation_config=config.get_evaluation_ML_config()
        evaluation=Evaluation(config=evaluation_config)
        evaluation.get_base_model()
        evaluation.evaluation()
        evaluation.log_into_mlflow() 


if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        baseModel=EvaluationPipeline()
        baseModel.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e