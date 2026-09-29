from autoreport.scheduler import start_scheduler
from pathlib import Path

import typer

from autoreport.ingestion import load_data
from autoreport.reports import (
    create_html_report,
    create_pdf_report,
    load_yaml_template,
)
from autoreport.scheduler import start_scheduler


app = typer.Typer(
    help="AutoReport - Automated Report & Analytics Generator"
)

TEMPLATES_DIR = Path("templates")
REPORTS_DIR = Path("reports")


@app.command()
def generate(
    template: str = typer.Option(
        ...,
        "--template",
        "-t",
        help="Path to the YAML report template."
    )
):
    """Generate HTML and PDF reports."""

    template_path = Path(template)

    if not template_path.exists():
        typer.echo(f"Template not found: {template_path}")
        raise typer.Exit(code=1)

    try:
        config = load_yaml_template(template_path)

        data_source = config["data"]["source"]

        typer.echo(f"Loading dataset: {data_source}")

        df = load_data(data_source)

        typer.echo(f"Rows: {len(df)}")
        typer.echo(f"Columns: {len(df.columns)}")

        report_name = template_path.stem

        html_output = REPORTS_DIR / f"{report_name}_report.html"
        pdf_output = REPORTS_DIR / f"{report_name}_report.pdf"

        create_html_report(
            template_path,
            df,
            html_output
        )

        create_pdf_report(
            template_path,
            df,
            pdf_output
        )

        typer.echo("Report generated successfully.")
        typer.echo(f"HTML: {html_output}")
        typer.echo(f"PDF: {pdf_output}")

    except Exception as error:
        typer.echo(f"Error: {error}")
        raise typer.Exit(code=1)


@app.command()
def validate(
    template: str = typer.Option(
        ...,
        "--template",
        "-t",
        help="Path to the YAML report template."
    )
):
    """Validate a YAML report template."""

    template_path = Path(template)

    if not template_path.exists():
        typer.echo(f"Template not found: {template_path}")
        raise typer.Exit(code=1)

    try:
        config = load_yaml_template(template_path)

        required_keys = [
            "name",
            "data",
            "sections",
            "charts",
        ]

        missing_keys = [
            key
            for key in required_keys
            if key not in config
        ]

        if missing_keys:
            typer.echo(
                f"Missing required fields: {missing_keys}"
            )
            raise typer.Exit(code=1)

        if "source" not in config["data"]:
            typer.echo("Missing data source.")
            raise typer.Exit(code=1)

        typer.echo("Template is valid.")

    except Exception as error:
        typer.echo(f"Invalid template: {error}")
        raise typer.Exit(code=1)


@app.command("list-templates")
def list_templates():
    """List available YAML report templates."""

    if not TEMPLATES_DIR.exists():
        typer.echo("Templates directory not found.")
        raise typer.Exit(code=1)

    templates = sorted(
        TEMPLATES_DIR.glob("*.yaml")
    )

    if not templates:
        typer.echo("No templates found.")
        return

    typer.echo("Available templates:")

    for template in templates:
        typer.echo(f"- {template.name}")


@app.command()
def schedule(
    template: str = typer.Option(
        ...,
        "--template",
        "-t",
        help="Path to the YAML report template."
    ),
    interval: int = typer.Option(
        60,
        "--interval",
        "-i",
        help="Interval between reports in minutes."
    )
):
    """Schedule recurring report generation."""

    template_path = Path(template)

    if not template_path.exists():
        typer.echo(
            f"Template not found: {template_path}"
        )
        raise typer.Exit(code=1)

    start_scheduler(
        template_path,
        interval
    )


if __name__ == "__main__":
    app()