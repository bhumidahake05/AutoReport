import pandas as pd

from autoreport.ingestion.excel_reader import read_excel
from autoreport.ingestion.datasource import DataSource


class ExcelDataSource(DataSource):
    """
    DataSource adapter for Excel files.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        return read_excel(self.file_path)