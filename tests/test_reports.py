import pandas as pd
import pytest

from autoreport.reports import (
    create_html_report,
    create_pdf_report,
)


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(
        {
            "product": ["A", "B"],
            "quantity": [10, 20],
        }
    )


def test_html_report_creation(tmp_path, sample_dataframe):

    output = tmp_path / "report.html"

    create_html_report(
        "templates/sales.yaml",
        sample_dataframe,
        output
    )

    assert output.exists()


def test_pdf_report_creation(tmp_path, sample_dataframe):

    output = tmp_path / "report.pdf"

    create_pdf_report(
        "templates/sales.yaml",
        sample_dataframe,
        output
    )

    assert output.exists()