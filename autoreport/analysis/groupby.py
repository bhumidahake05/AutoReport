import pandas as pd


def group_by_aggregate(
    df: pd.DataFrame,
    group_column: str,
    value_column: str,
    operation: str = "sum"
) -> pd.DataFrame:
    """
    Perform a group-by aggregation.
    """

    allowed_operations = [
        "sum",
        "mean",
        "median",
        "min",
        "max",
        "count"
    ]

    if operation not in allowed_operations:
        raise ValueError(
            f"Unsupported operation: {operation}. "
            f"Choose from {allowed_operations}."
        )

    result = (
        df.groupby(group_column)[value_column]
        .agg(operation)
    )

    return result