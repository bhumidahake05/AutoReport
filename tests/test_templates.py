from pathlib import Path

import yaml


def test_sales_template_exists():

    path = Path("templates/sales.yaml")

    assert path.exists()


def test_sales_template_is_valid():

    path = Path("templates/sales.yaml")

    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    assert "name" in config
    assert "data" in config
    assert "sections" in config
    assert "charts" in config


def test_sales_template_has_data_source():

    path = Path("templates/sales.yaml")

    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    assert "source" in config["data"]