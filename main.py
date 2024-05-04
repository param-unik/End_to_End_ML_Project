from e2emlproject.logging import logger
from e2emlproject.pipelines.data_ingestion_pipeline import DataIngestionPipelineStage
from e2emlproject.pipelines.data_validation_pipeline import DataValidationPipelineStage
from e2emlproject.pipelines.data_transformation_pipeline import (
    DataTransformationPipelineStage,
)

# STAGE_NAME = "data ingestion pipeline"
# STAGE_NAME = "data validation pipeline"
STAGE_NAME = "data transformation pipeline"


try:
    # logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    # obj = DataIngestionPipelineStage()
    # obj.data_ingestion_pipeline()
    # logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    # logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    # obj = DataValidationPipelineStage()
    # obj.data_validation_pipeline()
    # logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = DataTransformationPipelineStage()
    obj.data_transformation_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

except Exception as e:
    logger.exception(f"{STAGE_NAME} got failed!", e)
    raise e
