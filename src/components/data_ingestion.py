import os
import sys
from scr.exception import CustomException
from scr.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("datafolder", "train.csv")
    test_data_path: str=os.path.join("datafolder", "test.csv")
    ram_data_path: str=os.path.join("datafolder", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfing()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            