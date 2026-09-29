import sqlite3
import pandas as pd


data = {
    "product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor"
    ],
    "category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],
    "stock": [
        25,
        100,
        75,
        40
    ],
    "price": [
        60000,
        800,
        1500,
        12000
    ]
}

df = pd.DataFrame(data)

connection = sqlite3.connect("data/inventory.db")

df.to_sql(
    "inventory",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("SQLite database created successfully.")