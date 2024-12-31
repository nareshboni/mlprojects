import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Replace CustomException and logger with basic Python logging for debugging
import logging
logging.basicConfig(level=logging.INFO)

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entering the data ingestion method or component.")
        
        try:
            # Log the current working directory
            logging.info(f"Current working directory: {os.getcwd()}")

            # Ensure dataset path is absolute
            dataset_path = os.path.abspath("notebook\data\StudentsPerformance.csv")
            logging.info(f"Dataset path resolved to: {dataset_path}")

            # Validate dataset existence
            if not os.path.exists(dataset_path):
                logging.error(f"Dataset file not found at {dataset_path}")
                raise Exception(f"Dataset file not found at {dataset_path}")

            # Read the dataset
            logging.info("Reading the dataset...")
            df = pd.read_csv(dataset_path)
            logging.info(f"Dataset successfully read with shape: {df.shape}")

            # Create artifacts directory if it doesn't exist
            artifacts_dir = os.path.dirname(self.ingestion_config.train_data_path)
            os.makedirs(artifacts_dir, exist_ok=True)
            logging.info(f"Artifacts directory created or already exists: {artifacts_dir}")

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            # Train-test split
            logging.info("Initiating train-test split.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion process completed successfully.")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error(f"Error during data ingestion: {e}")
            raise e

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        obj.initiate_data_ingestion()
    except Exception as e:
        logging.error(f"Data ingestion failed: {e}")
