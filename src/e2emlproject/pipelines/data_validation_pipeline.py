from e2emlproject.config.configuration import ConfigurationManager
from e2emlproject.components.data_validation import DataValidation
from e2emlproject.logging import logger

STAGE_NAME = "Data Validation Pipeline stage"


class DataValidationPipelineStage:
    def __init__(self) -> None:
        pass

    def data_validation_pipeline(self):
        logger.info("Data Validation process started...")

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        logger.info("Data Validation process Completed!")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
        obj = DataValidationPipelineStage()
        obj.data_validation_pipeline()
        logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")
    except Exception as e:
        logger.exception("Data Validation Pipeline Failed!", e)
        raise e
