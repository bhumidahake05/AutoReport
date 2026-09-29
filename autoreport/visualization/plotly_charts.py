import pandas as pd
import plotly.express as px


def create_interactive_bar_chart(df, x_column, y_column, output_path):
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    fig.write_html(output_path)


def create_interactive_line_chart(df, x_column, y_column, output_path):
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        markers=True,
        title=f"{y_column} over {x_column}"
    )

    fig.write_html(output_path)


def create_interactive_pie_chart(
    df,
    label_column,
    value_column,
    output_path
):
    fig = px.pie(
        df,
        names=label_column,
        values=value_column,
        title=f"{value_column} Distribution"
    )

    fig.write_html(output_path)


def create_interactive_scatter_chart(
    df,
    x_column,
    y_column,
    output_path
):
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} vs {x_column}"
    )

    fig.write_html(output_path)