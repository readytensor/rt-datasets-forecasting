import os
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from typing import Tuple
import utils

import paths

def split_dataset(
        dataset: DataFrame, test_size: float = 0.2) -> Tuple[DataFrame, DataFrame]:
    """
    Splits the dataset into train and test set.
    
    Args:
        dataset (DataFrame): The dataset to be split.
        test_size (float): The proportion of the dataset to include in the test split.

    Returns:
        Tuple[DataFrame, DataFrame]: The train and test datasets.
    """
    train_df, test_df = train_test_split(dataset, test_size=test_size, random_state=42)
    return train_df, test_df

def save_train_data(
        train_df: DataFrame, dataset_name: str, processed_datasets_path: str) -> None:
    """
    Saves the train data to a CSV file.

    Args:
        train_df (DataFrame): The train dataset.
        dataset_name (str): The name of the dataset.
        processed_datasets_path (str): The path where the processed datasets are stored.
    """
    train_df.to_csv(os.path.join(
        processed_datasets_path, dataset_name, f"{dataset_name}_train.csv"), index=False)

def save_test_no_target_data(
        test_df: DataFrame,
        target_name: str,
        dataset_name: str,
        processed_datasets_path: str) -> None:
    """
    Saves the test data without the target column to a CSV file.

    Args:
        test_df (DataFrame): The test dataset.
        target_name (str): The name of the target column.
        dataset_name (str): The name of the dataset.
        processed_datasets_path (str): The path where the processed datasets are stored.
    """
    test_no_target_df = test_df.drop(target_name, axis=1)
    test_no_target_df.to_csv(
        os.path.join(processed_datasets_path, dataset_name, f"{dataset_name}_test.csv"), index=False)

def save_test_key_data(
        test_df: DataFrame,
        id_name: str,
        target_name: str,
        dataset_name: str,
        processed_datasets_path: str) -> None:
    """
    Saves the test key data to a CSV file.

    Args:
        test_df (DataFrame): The test dataset.
        id_name (str): The name of the ID column.
        target_name (str): The name of the target column.
        dataset_name (str): The name of the dataset.
        processed_datasets_path (str): The path where the processed datasets are stored.
    """
    test_key_df = test_df[[id_name, target_name]]
    test_key_df.to_csv(
        os.path.join(processed_datasets_path, dataset_name, f"{dataset_name}_test_key.csv"), index=False)


def create_train_test_testkey_files(dataset_cfg_path:str, processed_datasets_path:str) -> None:
    """
    Creates train, test, and test key files for each dataset marked for use in the metadata.
    """

    # Load the metadata
    dataset_metadata = utils.load_metadata(dataset_cfg_path)

    # Iterate through each dataset marked for use in the metadata
    for _, dataset_row in dataset_metadata[dataset_metadata['use_dataset'] == 1].iterrows():

        if dataset_row["use_dataset"] == 0:
            continue

        dataset_name = dataset_row["name"]
        print("Creating train/test files for dataset:", dataset_name)

        # Read dataset
        dataset = utils.load_dataset(dataset_name, processed_datasets_path)

        # Split the dataset
        train_df, test_df = split_dataset(dataset)

        # Save train/test data
        save_train_data(train_df, dataset_name, processed_datasets_path)

        # Save test data without target
        save_test_no_target_data(
            test_df, dataset_row["target_name"], dataset_name, processed_datasets_path)

        # Save test key data
        save_test_key_data(
            test_df, dataset_row["id_name"], dataset_row["target_name"], dataset_name, processed_datasets_path)


def run_train_test_testkey_files_gen():
    """Creates train, test, and test key files for each dataset marked for use in the metadata."""
    create_train_test_testkey_files(
        dataset_cfg_path=paths.dataset_cfg_path,
        processed_datasets_path=paths.processed_datasets_path
    )

if __name__ == "__main__":
    run_train_test_testkey_files_gen()
