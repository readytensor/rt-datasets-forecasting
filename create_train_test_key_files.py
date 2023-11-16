import os
import pandas as pd
from pandas import DataFrame
from typing import List
import sys

import utils
import paths



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
        past_covariates: List[str],
        dataset_name: str,
        processed_datasets_path: str) -> None:
    """
    Saves the test data without the target column to a CSV file.

    Args:
        test_df (DataFrame): The test dataset.
        target_name (str): The name of the target column.
        past_covariates (List[str]): The names of the past covariates.
        dataset_name (str): The name of the dataset.
        processed_datasets_path (str): The path where the processed datasets are stored.
    """
    test_no_target_df_no_past_cov = test_df.drop(columns=past_covariates + [target_name], axis=1)
    test_no_target_df_no_past_cov.to_csv(
        os.path.join(processed_datasets_path, dataset_name, f"{dataset_name}_test.csv"), index=False)


def get_past_covariates(schema: dict) -> list:
    """
    Extracts the names of all past covariates from a schema dictionary.

    Args:
        schema (dict): A schema represented as a dictionary.

    Returns:
        list: A list containing the names of all past covariates. Returns
        an empty list if there are no past covariates in the schema.

    Example:
        schema = { ... }  # your schema dictionary
        past_covariates = get_past_covariates(schema)
        print(past_covariates)
    """
    # Check if 'pastCovariates' exists in the schema and is a list
    if 'pastCovariates' in schema and isinstance(schema['pastCovariates'], list):
        # Extract and return the names of the past covariates
        return [covariate['name'] for covariate in schema['pastCovariates']]

    # Return an empty list if there are no past covariates
    return []


def save_test_key_data(
        test_df: DataFrame,
        id_name: str,
        time_name: str,
        target_name: str,
        dataset_name: str,
        processed_datasets_path: str) -> None:
    """
    Saves the test key data to a CSV file.

    Args:
        test_df (DataFrame): The test dataset.
        id_name (str): The name of the ID column.
        time_name (str): The name of the time column.
        target_name (str): The name of the target column.
        dataset_name (str): The name of the dataset.
        processed_datasets_path (str): The path where the processed datasets are stored.
    """
    test_key_df = test_df[[id_name, time_name, target_name]]
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

        # Read schema
        schema = utils.load_schema(dataset_name, processed_datasets_path)

        if schema["timeField"]["dataType"] != "INT":
            dataset[schema["timeField"]["name"]] = pd.to_datetime(dataset[schema["timeField"]["name"]])

        dataset_train_dfs = []
        dataset_test_dfs = []

        dataset_series_list = dataset[schema['idField']['name']].unique().tolist()
        forecast_length = schema['forecastLength']

        for series in dataset_series_list:
            series_df = dataset[dataset[schema['idField']['name']] == series]
            series_train_df = series_df.iloc[:-forecast_length]
            series_test_df = series_df.iloc[-forecast_length:]
            dataset_train_dfs.append(series_train_df)
            dataset_test_dfs.append(series_test_df)
            # print(series, series_df.shape, series_train_df.shape, series_test_df.shape)
        
        train_df = pd.concat(dataset_train_dfs)
        test_df = pd.concat(dataset_test_dfs)

        # Save train/test data
        save_train_data(train_df, dataset_name, processed_datasets_path)

        # Save test data without target
        past_covariates = get_past_covariates(schema)
        save_test_no_target_data(
            test_df,
            schema['forecastTarget']['name'],
            past_covariates,
            dataset_name,
            processed_datasets_path)

        # Save test key data
        save_test_key_data(
            test_df,
            schema['idField']['name'],
            schema['timeField']['name'],
            schema['forecastTarget']['name'],
            dataset_name,
            processed_datasets_path
        )


def run_train_test_testkey_files_gen():
    """Creates train, test, and test key files for each dataset marked for use in the metadata."""
    create_train_test_testkey_files(
        dataset_cfg_path=paths.dataset_cfg_path,
        processed_datasets_path=paths.processed_datasets_path
    )

if __name__ == "__main__":
    run_train_test_testkey_files_gen()
