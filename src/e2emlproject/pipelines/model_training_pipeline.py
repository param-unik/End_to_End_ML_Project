from e2emlproject.config.configuration import ConfigurationManager
from e2emlproject.components.model_trainer import ModelTrainer
from e2emlproject.logging import logger
from pathlib import Path

STAGE_NAME = "Model Training Pipeline stage"


class ModelTraininingPipelineStage:
    def __init__(self) -> None:
        pass

    def model_trainer_pipeline(self):

        try:
            logger.info("Model Training process started...")
            config = ConfigurationManager()
            model_training_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_training_config)
            model_trainer.train_model()
            logger.info("Model Training process Completed!")
        except Exception as e:
            logger.exception("Model Training Pipeline Failed!")
            print(e)


if __name__ == "__main__":
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = ModelTraininingPipelineStage()
    obj.model_trainer_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")
