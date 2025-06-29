# src/data_pipeline/pdf.py

import pandas as pd
import re
from PyPDF2 import PdfReader

def extract_may_2024_prices(pdf_path: str, month: str, year: int) -> pd.DataFrame:
    """
    Extracts fuel price data from the May 2024 PDF and formats it like the Excel files.

    Args:
        pdf_path (str): Path to the May 2024 PDF file.
        month (str): Month string to tag the data (e.g., "May").
        year (int): Year to tag the data (e.g., 2024).

    Returns:
        pd.DataFrame: A cleaned DataFrame with the same structure as Excel results.
    """
    reader = PdfReader(pdf_path)
    text = reader.pages[7].extract_text()  # Page 8 (0-indexed)

    # Split lines and discard headers and region summaries
    lines = text.split('\n')
    raw_data_lines = [
        line.strip() for line in lines
        if line.strip() and not re.match(r"^(NORTH|SOUTH|Grand Total|APPENDIX)", line)
    ]

    records = []
    for line in raw_data_lines:
        numbers = re.findall(r'\d+\.\d+', line)
        if len(numbers) == 5:
            try:
                # Extract state name by removing numbers
                state_part = line.rsplit(numbers[0], 1)[0].strip()
                if not state_part or state_part[-1].isdigit():
                    state_part = re.split(r'\d', line)[0].strip()
                row = [state_part] + [float(n) for n in numbers[:3]]  # Only 3 price columns
                records.append(row)
            except Exception as e:
                print(f"⚠️ Failed to process line: {line}\nError: {e}")
                continue

    # Build final DataFrame
    df = pd.DataFrame(records, columns=[
        "State", "Prices_of_last_year", "Prices_of_last_month", "Prices"
    ])
    df["Month"] = month
    df["Year"] = year

    return df
