from src.DataScience import logger
from src.DataScience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline  
from src.DataScience.pipeline.data_validation_pipeline import DataValidaionTrainingPipeline

STAGE_NAME = "DataIngestionTrainingPipeline"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "DataValidationTrainingPipeline"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidaionTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e