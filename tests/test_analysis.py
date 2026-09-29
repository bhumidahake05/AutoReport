import pandas as pd
import pytest

from autoreport.analysis import (
    calculate_mean,
    calculate_median,
    calculate_std,
    calculate_percentile,
    group_by_aggregate,
)


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(
        {
            "product": [
                "A",
                "A",
                "B",
                "B",
            ],
            "quantity": [
                10,
                20,
                30,
                40,
            ],
        }
    )


def test_mean(sample_dataframe):
    result = calculate_mean(
        sample_dataframe,
        "quantity"
    )

    assert result == 25


def test_median(sample_dataframe):
    result = calculate_median(
        sample_dataframe,
        "quantity"
    )

    assert result == 25


def test_standard_deviation(sample_dataframe):
    result = calculate_std(
        sample_dataframe,
        "quantity"
    )

    assert result > 0


def test_percentile(sample_dataframe):
    result = calculate_percentile(
        sample_dataframe,
        "quantity",
        75
    )

    assert result == 32.5


def test_group_by_sum(sample_dataframe):
    result = group_by_aggregate(
        sample_dataframe,
        "product",
        "quantity",
        "sum"
    )

    assert result.loc["A"] == 30
    assert result.loc["B"] == 70