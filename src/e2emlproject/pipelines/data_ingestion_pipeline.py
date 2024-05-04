from e2emlproject.config.configuration import ConfigurationManager
from e2emlproject.components.data_ingestion import DataIngestion
from e2emlproject.logging import logger

STAGE_NAME = "Data Ingestion Pipeline stage"


class DataIngestionPipelineStage:
    def __init__(self) -> None:
        pass

    def data_ingestion_pipeline(self):
        logger.info("Data Ingestion process started...")

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingesttion = DataIngestion(config=data_ingestion_config)
        data_ingesttion.download_file()
        data_ingesttion.extract_zip_file()
        logger.info("Data Ingestion process Completed!")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} started! <<<<<<<<")
        obj = DataIngestionPipelineStage()
        obj.data_ingestion_pipeline()
        logger.info(f">>>>>>> {STAGE_NAME} completed! <<<<<<<<")
    except Exception as e:
        logger.exception("Data Ingestion Pipeline Failed!", e)
        raise e
