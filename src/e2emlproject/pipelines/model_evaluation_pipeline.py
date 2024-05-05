from e2emlproject.config.configuration import ConfigurationManager
from e2emlproject.components.model_evaluator import ModelEvaluator
from e2emlproject.logging import logger


STAGE_NAME = "Model Evalution Pipeline stage"


class ModelEvaluationPipelineStage:
    def __init__(self) -> None:
        pass

    def model_evaluation_pipeline(self):
        try:
            logger.info("Model Evaluation process started!:")
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluator(config=model_evaluation_config)
            model_evaluation.save_results()
            logger.info("Model Evaluation process completed!")
        except Exception as e:
            raise e


if __name__ == "__main__":
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = ModelEvaluationPipelineStage()
    obj.model_evaluation_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")
