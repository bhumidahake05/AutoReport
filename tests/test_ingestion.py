from pathlib import Path

import pandas as pd
import pytest

from autoreport.ingestion import load_data


DATA_FILE = Path("data/sales.csv")


def test_csv_loads_successfully():
    df = load_data(DATA_FILE)

    assert isinstance(df, pd.DataFrame)


def test_csv_has_expected_rows():
    df = load_data(DATA_FILE)

    assert len(df) == 10


def test_csv_has_expected_columns():
    df = load_data(DATA_FILE)

    assert list(df.columns) == [
        "date",
        "product",
        "category",
        "quantity",
        "price",
    ]


def test_missing_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_data("data/does_not_exist.csv")


def test_unsupported_file_raises_error():
    with pytest.raises(ValueError):
        load_data("data/test.txt")