from pathlib import Path
import sqlite3
import pandas as pd


def read_sqlite(
    file_path: str,
    table_name: str
) -> pd.DataFrame:
    """
    Read a table from a SQLite database.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() not in [".db", ".sqlite", ".sqlite3"]:
        raise ValueError("The provided file is not a SQLite database.")

    connection = sqlite3.connect(path)

    try:
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(query, connection)
    finally:
        connection.close()