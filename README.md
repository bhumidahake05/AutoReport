# AutoReport

AutoReport is a CLI-driven automated report and analytics generator built with Python.

## Features

- CSV data ingestion
- Excel data ingestion
- JSON data ingestion
- SQLite data ingestion
- Statistical analysis
- Group-by analysis
- Trend detection
- Moving averages
- Growth rates
- Z-score anomaly detection
- IQR anomaly detection
- Static charts
- Interactive Plotly charts
- YAML report templates
- HTML reports
- PDF reports
- Scheduled report generation

## Project Structure

D:\internship\AutoReport
│
├── autoreport
│   ├── __init__.py
│   ├── cli.py
│   ├── scheduler.py
│   │
│   ├── ingestion
│   │   ├── __init__.py
│   │   ├── datasource.py
│   │   ├── factory.py
│   │   ├── loader.py
│   │   ├── csv_reader.py
│   │   ├── excel_reader.py
│   │   ├── json_reader.py
│   │   ├── sqlite_reader.py
│   │   ├── csv_adapter.py
│   │   ├── excel_adapter.py
│   │   ├── json_adapter.py
│   │   ├── sqlite_adapter.py
│   │   └── validator.py
│   │
│   ├── analysis
│   │   ├── __init__.py
│   │   ├── statistics.py
│   │   ├── groupby.py
│   │   ├── trends.py
│   │   └── anomalies.py
│   │
│   ├── visualization
│   │   ├── __init__.py
│   │   ├── charts.py
│   │   └── plotly_charts.py
│   │
│   └── reports
│       ├── __init__.py
│       ├── html_report.py
│       ├── pdf_report.py
│       └── templates
│           └── report.html
│
├── data
│   ├── sales.csv
│   ├── sales.xlsx
│   ├── inventory.json
│   └── inventory.db
│
├── templates
│   ├── sales.yaml
│   ├── hr.yaml
│   └── inventory.yaml
│
├── reports
│   ├── charts
│   └── interactive
│
├── tests
│
├── requirements.txt
├── pyproject.toml
└── README.md
