import os
from src.DataScience import logger
from src.DataScience.entity.config_entity import (DataIngestionconfig,DataValidationConfig)
from src.DataScience.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.DataScience.utils.common import read_yaml,create_directories

import pandas as pd

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            expected_schema = self.config.all_schema

            # Check if all required columns exist
            for col in expected_schema:
                if col not in all_cols:
                    validation_status = False
                    print(f"Missing column: {col}")

            # Check data types
            for col, expected_dtype in expected_schema.items():
                if col in data.columns:
                    actual_dtype = str(data[col].dtype)
                    if actual_dtype != expected_dtype:
                        print(f"Data type mismatch for column '{col}': expected '{expected_dtype}', got '{actual_dtype}'")
                        validation_status = False

            # Write final validation status
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e