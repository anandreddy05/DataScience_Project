import os
import urllib.request as request
from src.DataScience import logger
import zipfile
from src.DataScience.entity.config_entity import (DataIngestionconfig)

class DataIngestionComponent:
    def __init__(self,config:DataIngestionconfig):
        self.config=config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        zip_path = self.config.local_data_file

        # 🔍 Validate before extracting
        if not zipfile.is_zipfile(zip_path):
            raise Exception(f"The file at '{zip_path}' is not a valid zip file. Check download or URL.")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Successfully extracted ZIP to {unzip_path}")