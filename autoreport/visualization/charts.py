import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_bar_chart(df, x_column, y_column, output_path):
    plt.figure(figsize=(8, 5))

    plt.bar(df[x_column], df[y_column])

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} by {x_column}")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def create_line_chart(df, x_column, y_column, output_path):
    plt.figure(figsize=(8, 5))

    plt.plot(df[x_column], df[y_column], marker="o")

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} over {x_column}")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def create_pie_chart(df, label_column, value_column, output_path):
    plt.figure(figsize=(7, 7))

    plt.pie(
        df[value_column],
        labels=df[label_column],
        autopct="%1.1f%%"
    )

    plt.title(f"{value_column} Distribution")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def create_scatter_chart(df, x_column, y_column, output_path):
    plt.figure(figsize=(8, 5))

    plt.scatter(df[x_column], df[y_column])

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} vs {x_column}")

    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def create_heatmap(df, output_path):
    numeric_df = df.select_dtypes(include="number")

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()


def create_histogram(df, column, output_path):
    plt.figure(figsize=(8, 5))

    plt.hist(df[column], bins=10)

    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {column}")

    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()