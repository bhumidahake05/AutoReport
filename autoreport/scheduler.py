from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler

from autoreport.ingestion import load_data
from autoreport.reports import (
    create_html_report,
    create_pdf_report,
    load_yaml_template,
)


def generate_scheduled_report(template_path):
    template_path = Path(template_path)

    config = load_yaml_template(template_path)

    data_source = config["data"]["source"]

    print(f"Loading dataset: {data_source}")

    df = load_data(data_source)

    report_name = template_path.stem

    html_output = (
        Path("reports") /
        f"{report_name}_scheduled.html"
    )

    pdf_output = (
        Path("reports") /
        f"{report_name}_scheduled.pdf"
    )

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

    print("Scheduled report generated.")
    print(f"HTML: {html_output}")
    print(f"PDF: {pdf_output}")


def start_scheduler(template_path, interval_minutes=60):
    scheduler = BlockingScheduler()

    scheduler.add_job(
        generate_scheduled_report,
        "interval",
        minutes=interval_minutes,
        args=[template_path],
    )

    print(
        f"Scheduler started. "
        f"Report will run every {interval_minutes} minutes."
    )

    try:
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler stopped.")