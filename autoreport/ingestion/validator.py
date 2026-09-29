import pandas as pd


def validate_dataframe(df: pd.DataFrame, required_columns=None) -> pd.DataFrame:
    """
    Validate the input DataFrame and check required columns.
    """

    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty.")

    # Check required columns
    if required_columns:
        missing_columns = [
            column for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

    return df




