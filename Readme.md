# Nigerian Fuel Price Analysis
## STILL IN DEVELOPMENT

## Project Overview
Analysis of fuel price trends across Nigeria, examining regional variations, temporal patterns, and potential correlations with economic indicators.

## Project Structure
```plaintext

nigerian-fuel-price-analysis/
│
├── data/
│   ├── raw_data/        # Original, immutable data
│   |   ├── 2025/
|   |   ├── 2024/
│   |   ├── 2023/
│   |   └── 2022/
|   |      
│   ├── processed_data/ # Cleaned, transformed data
│   └── external/       # Third-party data sources
│
├── notebooks/          # Jupyter notebooks
├── src/                # Python source files
│   ├── __init__.py
│   ├── data_scripts/           # Data processing scripts
│   └── visualization_scipts/  # Visualization scripts
│
├── results/            # Generated analysis reports
├── .gitignore          # Git ignore file
├── README.md           # Project overview
└── requirements.txt    # Dependencies
```

## Data Sources

- [NBS Data](www.nbs.com)


## Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate environment
4. Install dependencies: `pip install -r requirements.txt`

## Usage
Run Jupyter notebooks from the `notebooks/` directory.

## Contributing
Pull requests welcome. Please open an issue first to discuss changes.