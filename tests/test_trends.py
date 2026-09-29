import pandas as pd

from autoreport.analysis import (
    prepare_time_series,
    calculate_moving_average,
    calculate_growth_rate,
)


def test_prepare_time_series():

    df = pd.DataFrame(
        {
            "date": [
                "2026-01-03",
                "2026-01-01",
                "2026-01-02",
            ],
            "quantity": [
                30,
                10,
                20,
            ],
        }
    )

    result = prepare_time_series(
        df,
        "date"
    )

    assert result.iloc[0]["quantity"] == 10


def test_moving_average():

    df = pd.DataFrame(
        {
            "quantity": [
                10,
                20,
                30,
            ]
        }
    )

    result = calculate_moving_average(
        df,
        "quantity",
        window=2
    )

    assert result.iloc[1]["moving_average"] == 15


def test_growth_rate():

    df = pd.DataFrame(
        {
            "quantity": [
                10,
                20,
            ]
        }
    )

    result = calculate_growth_rate(
        df,
        "quantity"
    )

    assert result.iloc[1]["growth_rate"] == 100