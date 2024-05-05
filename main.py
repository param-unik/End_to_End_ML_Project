from e2emlproject.logging import logger
from e2emlproject.pipelines.data_ingestion_pipeline import DataIngestionPipelineStage
from e2emlproject.pipelines.data_validation_pipeline import DataValidationPipelineStage
from e2emlproject.pipelines.data_transformation_pipeline import (
    DataTransformationPipelineStage,
)
from e2emlproject.pipelines.model_training_pipeline import ModelTraininingPipelineStage
from e2emlproject.pipelines.model_evaluation_pipeline import (
    ModelEvaluationPipelineStage,
)


try:
    STAGE_NAME = "Data ingestion pipeline"
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = DataIngestionPipelineStage()
    obj.data_ingestion_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    STAGE_NAME = "Data validation pipeline"
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = DataValidationPipelineStage()
    obj.data_validation_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    STAGE_NAME = "Data transformation pipeline"
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = DataTransformationPipelineStage()
    obj.data_transformation_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    STAGE_NAME = "Model training pipeline"
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = ModelTraininingPipelineStage()
    obj.model_trainer_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

    STAGE_NAME = "Model evaluation pipeline"
    logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
    obj = ModelEvaluationPipelineStage()
    obj.model_evaluation_pipeline()
    logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")

except Exception as e:
    logger.exception(f"{STAGE_NAME} got failed!", e)
    raise e
