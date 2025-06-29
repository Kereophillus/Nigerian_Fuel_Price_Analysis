# src/data_pipeline/excel.py

import pandas as pd

def clean_excel_file(file_path: str, metadata_row: pd.Series) -> pd.DataFrame:
    """
    Cleans an Excel file using metadata-driven instructions.

    Args:
        file_path (str): Full path to the Excel file.
        metadata_row (pd.Series): Row from metadata.csv.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    sheet_name = int(metadata_row["sheet_name"]) if not pd.isna(metadata_row["sheet_name"]) else 0
    start_row = int(metadata_row["start_row"])    # Excel-style (e.g., 3)
    end_row = int(metadata_row["end_row"])        # Excel-style (e.g., 45)
    usecols = metadata_row["usecols"]
    column_names = [c.strip() for c in metadata_row["column_names"].split(",")]
    skip_rows_str = metadata_row["skip_rows"]

    # Compute total block range
    total_rows = end_row - start_row + 1

    # Prepare skiprows (0-based index)
    skip_rows_excel = [int(r.strip()) for r in skip_rows_str.split(',')] if pd.notnull(skip_rows_str) else []
    skip_rows_zero_indexed = [r - 1 for r in skip_rows_excel]

    # Final skiprows includes rows before the block and any skipped within it
    final_skiprows = [
        r for r in range(end_row)
        if r < start_row - 1 or r in skip_rows_zero_indexed
    ]

    # Read and clean Excel
    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        skiprows=final_skiprows,
        nrows=total_rows,
        usecols=usecols,
        header=None
    )

    df.columns = column_names[:len(df.columns)]
    df["Month"] = metadata_row["month"]
    df["Year"] = int(metadata_row["year"])

    return df
