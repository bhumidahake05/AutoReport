from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

import yaml


def load_yaml_template(template_path):
    with open(template_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_pdf_report(
    template_path,
    dataframe,
    output_path
):
    config = load_yaml_template(template_path)

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    story = []

    # Report title
    story.append(
        Paragraph(
            config["name"],
            styles["Title"]
        )
    )

    story.append(Spacer(1, 15))

    # Description
    description = config.get("description", "")

    story.append(
        Paragraph(
            description,
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    # Sections
    for section in config.get("sections", []):

        story.append(
            Paragraph(
                section["name"],
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"Section type: {section['type']}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 12))

    # Dataset
    story.append(
        Paragraph(
            "Dataset",
            styles["Heading2"]
        )
    )

    columns = list(dataframe.columns)

    table_data = [columns]

    for row in dataframe.itertuples(index=False):

        table_data.append(
            list(row)
        )

    table = Table(
        table_data,
        repeatRows=1
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.black
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),
            ]
        )
    )

    story.append(table)

    story.append(Spacer(1, 20))

    # Chart information
    story.append(
        Paragraph(
            "Charts",
            styles["Heading2"]
        )
    )

    for chart in config.get("charts", []):

        chart_title = chart.get(
            "title",
            chart["type"].title()
        )

        story.append(
            Paragraph(
                chart_title,
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                f"Chart type: {chart['type']}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 8))

    document.build(story)

    return output_path