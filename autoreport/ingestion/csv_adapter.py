import pandas as pd

from autoreport.ingestion.csv_reader import read_csv
from autoreport.ingestion.datasource import DataSource


class CSVDataSource(DataSource):
    """
    DataSource adapter for CSV files.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        return read_csv(self.file_path)