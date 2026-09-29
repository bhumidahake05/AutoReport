from abc import ABC, abstractmethod
import pandas as pd


class DataSource(ABC):
    """
    Base interface for all data sources.
    """

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        Load data and return a Pandas DataFrame.
        """
        raise NotImplementedError