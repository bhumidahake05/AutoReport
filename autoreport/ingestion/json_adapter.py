import pandas as pd

from autoreport.ingestion.json_reader import read_json
from autoreport.ingestion.datasource import DataSource


class JSONDataSource(DataSource):
    """
    DataSource adapter for JSON files.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        return read_json(self.file_path)