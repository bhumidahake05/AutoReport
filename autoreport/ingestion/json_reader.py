from pathlib import Path
import pandas as pd


def read_json(file_path: str) -> pd.DataFrame:
    """
    Read a JSON file and return it as a Pandas DataFrame.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".json":
        raise ValueError("The provided file is not a JSON file.")

    return pd.read_json(path)