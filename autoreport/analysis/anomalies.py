import pandas as pd


def detect_zscore_anomalies(
    df: pd.DataFrame,
    column: str,
    threshold: float = 3.0
) -> pd.DataFrame:
    """
    Detect anomalies using the Z-score method.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' not found."
        )

    if threshold <= 0:
        raise ValueError(
            "Threshold must be greater than 0."
        )

    result = df.copy()

    mean = result[column].mean()
    std = result[column].std()

    if std == 0:
        result["z_score"] = 0.0
        result["zscore_anomaly"] = False
        return result

    result["z_score"] = (
        (result[column] - mean) / std
    )

    result["zscore_anomaly"] = (
        result["z_score"].abs() > threshold
    )

    return result


def detect_iqr_anomalies(
    df: pd.DataFrame,
    column: str,
    multiplier: float = 1.5
) -> pd.DataFrame:
    """
    Detect outliers using the IQR method.
    """

    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' not found."
        )

    if multiplier <= 0:
        raise ValueError(
            "Multiplier must be greater than 0."
        )

    result = df.copy()

    q1 = result[column].quantile(0.25)
    q3 = result[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (
        multiplier * iqr
    )

    upper_bound = q3 + (
        multiplier * iqr
    )

    result["iqr_lower_bound"] = lower_bound
    result["iqr_upper_bound"] = upper_bound

    result["iqr_anomaly"] = (
        (result[column] < lower_bound)
        |
        (result[column] > upper_bound)
    )

    return result