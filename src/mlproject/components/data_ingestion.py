from dataclasses import dataclass
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            
            current_dir = os.path.dirname(os.path.abspath(__file__))  # src/mlproject/components
            project_root = os.path.abspath(os.path.join(current_dir, '../../..'))  # go 3 levels up
            raw_csv_path = os.path.join(project_root, 'notebook', 'data', 'raw.csv')
            df = pd.read_csv(raw_csv_path)

            # Create artifacts folder if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data to artifacts
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved at: %s", self.ingestion_config.raw_data_path)

            if not os.path.exists(raw_csv_path):
              raise FileNotFoundError(f"{raw_csv_path} does not exist")


            # Split into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully.")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error("Error in data ingestion: %s", e)
            raise CustomException(e, sys)
