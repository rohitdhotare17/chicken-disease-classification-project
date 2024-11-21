import os
import zipfile
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


import os
import zipfile
import urllib.request as request
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to get file size
def get_size(path: Path) -> str:
    size_in_bytes = path.stat().st_size
    size_in_mb = size_in_bytes / (1024 * 1024)
    return f"{size_in_mb:.2f} MB"

# DataIngestionConfig Class
class DataIngestionConfig:
    def __init__(self, source_URL: str, local_data_file: str, unzip_dir: str):
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

# DataIngestion Class
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! With the following info: \n{headers}")
        else:
            logger.info(
                f"File already exists. Size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted all files to {unzip_path}")
