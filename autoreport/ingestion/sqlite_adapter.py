import pandas as pd

from autoreport.ingestion.sqlite_reader import read_sqlite
from autoreport.ingestion.datasource import DataSource


class SQLiteDataSource(DataSource):
    """
    DataSource adapter for SQLite databases.
    """

    def __init__(self, file_path: str, table_name: str):
        self.file_path = file_path
        self.table_name = table_name

    def load(self) -> pd.DataFrame:
        return read_sqlite(
            self.file_path,
            self.table_name
        )