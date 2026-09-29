from pathlib import Path
import pandas as pd

from autoreport.ingestion.csv_reader import read_csv
from autoreport.ingestion.excel_reader import read_excel
from autoreport.ingestion.validator import validate_dataframe


def load_data(
    file_path: str,
    required_columns: list[str] | None = None
) -> pd.DataFrame:
    """
    Load data from CSV or Excel files.
    """

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension not in [".csv", ".xlsx", ".xls"]:
        raise ValueError(
            "Unsupported file format. "
            "Supported formats: CSV, XLSX, XLS."
        )

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if extension == ".csv":
        df = read_csv(file_path)

    elif extension in [".xlsx", ".xls"]:
        df = read_excel(file_path)

    validate_dataframe(df, required_columns)

    return df