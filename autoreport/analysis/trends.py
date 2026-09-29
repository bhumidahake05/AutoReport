import pandas as pd


def prepare_time_series(
    df: pd.DataFrame,
    date_column: str
) -> pd.DataFrame:
    """
    Prepare data for time-series analysis.
    """

    if date_column not in df.columns:
        raise ValueError(
            f"Column '{date_column}' not found."
        )

    result = df.copy()

    result[date_column] = pd.to_datetime(
        result[date_column]
    )

    result = result.sort_values(
        by=date_column
    ).reset_index(drop=True)

    return result


def calculate_moving_average(
    df: pd.DataFrame,
    value_column: str,
    window: int = 3
) -> pd.DataFrame:
    """
    Calculate a moving average for a time-series column.
    """

    if window <= 0:
        raise ValueError("Window must be greater than 0.")

    if value_column not in df.columns:
        raise ValueError(
            f"Column '{value_column}' not found."
        )

    result = df.copy()

    result["moving_average"] = (
        result[value_column]
        .rolling(window=window)
        .mean()
    )

    return result


def calculate_growth_rate(
    df: pd.DataFrame,
    value_column: str
) -> pd.DataFrame:
    """
    Calculate percentage growth between consecutive values.
    """

    if value_column not in df.columns:
        raise ValueError(
            f"Column '{value_column}' not found."
        )

    result = df.copy()

    result["growth_rate"] = (
        result[value_column]
        .pct_change() * 100
    )

    return result