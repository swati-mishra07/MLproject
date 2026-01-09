import os
from dotenv import load_dotenv
import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine
from mlproject.exception import CustomException
from mlproject.logger import logging


import pickle
import numpy as np


load_dotenv()

def read_sql_data():
    try:
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")

        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{database}"
        )

        df = pd.read_sql("SELECT * FROM students", engine)
        return df

    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved successfully at {file_path}")

            

    except Exception as e:
        raise CustomException(e, sys)