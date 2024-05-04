import os
import urllib.request as request
import zipfile
from pathlib import Path
from e2emlproject.logging import logger
from e2emlproject.utils.common import get_size
from e2emlproject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(
                f"Downloaded {filename} of size {get_size(Path(self.config.local_data_file))} from {self.config.source_URL} with the following info: \n {headers}!!"
            )
        else:
            logger.warning(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}."
            )

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        logger.info("Zip extration started!")
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info("Zip extraction completed!")
