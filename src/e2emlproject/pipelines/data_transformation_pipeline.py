from e2emlproject.config.configuration import ConfigurationManager
from e2emlproject.components.data_transformation import DataTransformation
from e2emlproject.logging import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Pipeline stage"


class DataTransformationPipelineStage:
    def __init__(self) -> None:
        pass

    def data_transformation_pipeline(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                for line in file:
                    message, status = line.strip().split(":")
                    if status.strip() == "False":
                        break
            if status.strip() != "False":
                logger.info("Data Transformation process started...")
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()

                data_transformation = DataTransformation(
                    config=data_transformation_config
                )
                data_transformation.train_test_spliting()
                logger.info("Data Transformation process Completed!")
            else:
                logger.error(
                    "Data Transformation Pipeline Failed!, Check the status.txt"
                )
                logger.error(f"{message} {status}")
                raise Exception("Data is not valid check status.txt")
        except Exception as e:
            print(e)
