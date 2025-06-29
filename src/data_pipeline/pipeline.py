# src/data_pipeline/pipeline.py

import os
import pandas as pd

from data_pipeline.excel import clean_excel_file
from data_pipeline.pdf import extract_may_2024_prices
from utils.io import load_metadata

def run_pipeline(metadata_csv_path: str, raw_data_dir: str) -> dict:
    """
    Master function that runs the entire pipeline.

    Args:
        metadata_csv_path (str): Path to metadata.csv
        raw_data_dir (str): Base directory where raw files are stored (e.g. "data/raw_data/")

    Returns:
        dict: Dictionary of cleaned DataFrames keyed by cleaned file name.
    """
    metadata = load_metadata(metadata_csv_path)
    cleaned_data = {}

    for _, row in metadata.iterrows():
        file_name = row["file_name"]
        extension = str(row["extension"]).strip().lower()
        year = str(row["year"])
        month = str(row["month"])

        file_path = os.path.join(raw_data_dir, year, file_name)
        key_name = os.path.splitext(file_name)[0]  # Use base name without extension

        print(f"📦 Processing: {file_name}")

        try:
            if extension == "xlsx" or extension == "xls":
                df = clean_excel_file(file_path, row)
            elif extension == "pdf":
                df = extract_may_2024_prices(file_path, month, int(year))
            else:
                print(f"⚠️ Unsupported file type: {extension}")
                continue

            cleaned_data[key_name] = df
        except Exception as e:
            print(f"❌ Failed to process {file_name}: {e}")

    return cleaned_data
