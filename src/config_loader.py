import pandas as pd
import yaml
import os


DEFAULT_BUDGETS = {
    "Fuel": 1000,
    "Maintenance": 500,
    "Food": 300,
    "Insurance": 400,
    "Other": 200
}


def load_budgets(path="config/budgets.csv"):
    if not os.path.exists(path):
        print("⚠ Budget file not found. Using default budgets.")
        return DEFAULT_BUDGETS

    try:
        df = pd.read_csv(path)
        return dict(zip(df["category"], df["budget"]))
    except Exception as e:
        print(f"⚠ Error loading budgets: {e}")
        return DEFAULT_BUDGETS

