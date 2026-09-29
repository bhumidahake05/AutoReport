from autoreport.ingestion.datasource import DataSource
from autoreport.ingestion.csv_adapter import CSVDataSource
from autoreport.ingestion.excel_adapter import ExcelDataSource
from autoreport.ingestion.json_adapter import JSONDataSource
from autoreport.ingestion.sqlite_adapter import SQLiteDataSource


def create_data_source(
    file_path: str,
    table_name: str | None = None
) -> DataSource:
    """
    Create the appropriate DataSource adapter.
    """

    extension = file_path.lower().split(".")[-1]

    if extension == "csv":
        return CSVDataSource(file_path)

    if extension in ["xlsx", "xls"]:
        return ExcelDataSource(file_path)

    if extension == "json":
        return JSONDataSource(file_path)

    if extension in ["db", "sqlite", "sqlite3"]:
        if not table_name:
            raise ValueError(
                "table_name is required for SQLite databases."
            )

        return SQLiteDataSource(
            file_path,
            table_name
        )

    raise ValueError(
        "Unsupported data source. "
        "Supported: CSV, Excel, JSON, SQLite."
    )
