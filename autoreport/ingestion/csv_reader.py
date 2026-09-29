from pathlib import Path
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read a CSV file and return it as a Pandas DataFrame.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("The provided file is not a CSV file.")

    return pd.read_csv(path)