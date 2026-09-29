import pandas as pd

from autoreport.analysis import (
    detect_zscore_anomalies,
    detect_iqr_anomalies,
)


def test_zscore_columns_are_created():

    df = pd.DataFrame(
        {
            "quantity": [
                10,
                10,
                10,
                100,
            ]
        }
    )

    result = detect_zscore_anomalies(
        df,
        "quantity"
    )

    assert "z_score" in result.columns
    assert "zscore_anomaly" in result.columns


def test_iqr_columns_are_created():

    df = pd.DataFrame(
        {
            "quantity": [
                10,
                20,
                30,
                100,
            ]
        }
    )

    result = detect_iqr_anomalies(
        df,
        "quantity"
    )

    assert "iqr_lower_bound" in result.columns
    assert "iqr_upper_bound" in result.columns
    assert "iqr_anomaly" in result.columns