from pathlib import Path
import pandas as pd


def read_excel(file_path: str) -> pd.DataFrame:
    """
    Read an Excel file and return it as a Pandas DataFrame.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() not in [".xlsx", ".xls"]:
        raise ValueError("The provided file is not an Excel file.")

    return pd.read_excel(path)