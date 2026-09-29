from pathlib import Path

import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader


def load_yaml_template(template_path):
    with open(template_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_html_report(
    template_path,
    dataframe,
    output_path
):
    config = load_yaml_template(template_path)

    template_directory = Path(__file__).parent / "templates"

    environment = Environment(
        loader=FileSystemLoader(template_directory)
    )

    template = environment.get_template("report.html")

    html = template.render(
        report_name=config["name"],
        description=config.get("description", ""),
        sections=config.get("sections", []),
        charts=config.get("charts", []),
        rows=dataframe.to_dict(orient="records"),
        columns=list(dataframe.columns)
    )

    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        html,
        encoding="utf-8"
    )

    return output_path