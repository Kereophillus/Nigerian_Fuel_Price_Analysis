# src/utils/io.py

import pandas as pd
import os

def load_metadata(csv_path: str) -> pd.DataFrame:
    """
    Load the metadata CSV that guides how each file should be processed.

    Args:
        csv_path (str): Path to the metadata.csv file.

    Returns:
        pd.DataFrame: Parsed metadata as a DataFrame.
    """
    try:
        metadata = pd.read_csv(csv_path)
        return metadata
    except Exception as e:
        raise RuntimeError(f"Failed to load metadata: {e}")


def save_dataframe(df: pd.DataFrame, output_path: str):
    """
    Save a DataFrame to CSV format (without index), ensuring the directory exists.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): Path to save the CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Saved to: {output_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to save DataFrame: {e}")
