from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestionConfig
import sys


if __name__ == "__main__":
    logging.info("The application has started.")


    try:
       # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        

    except Exception as e:
        logging.info("Custom exception is being raised.")
        raise CustomException(e, sys)