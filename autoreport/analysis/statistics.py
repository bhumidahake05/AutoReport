import pandas as pd


def calculate_mean(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the mean of a numeric column.
    """
    return float(df[column].mean())


def calculate_median(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the median of a numeric column.
    """
    return float(df[column].median())


def calculate_std(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the standard deviation of a numeric column.
    """
    return float(df[column].std())


def calculate_percentile(
    df: pd.DataFrame,
    column: str,
    percentile: float
) -> float:
    """
    Calculate a percentile for a numeric column.

    percentile must be between 0 and 100.
    """

    if not 0 <= percentile <= 100:
        raise ValueError(
            "Percentile must be between 0 and 100."
        )

    return float(
        df[column].quantile(percentile / 100)
    )


def summary_statistics(
    df: pd.DataFrame,
    columns: list[str] | None = None
) -> pd.DataFrame:
    """
    Generate summary statistics for numeric columns.
    """

    if columns:
        data = df[columns]
    else:
        data = df.select_dtypes(include="number")

    if data.empty:
        raise ValueError(
            "No numeric columns available for analysis."
        )

    return data.describe().T