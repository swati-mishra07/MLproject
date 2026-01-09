import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
from mlproject.components.data_transformation import DataTransformationConfig, DataTransformation
from mlproject.utils import save_object
from mlproject.exception import CustomException
from mlproject.logger import logging

import sys


if __name__ == "__main__":
    logging.info("The application has started.")


    try:
         #data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

       

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
      