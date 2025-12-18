import pandas as pd


REQUIRED_COLUMNS = {"date", "description", "amount"}


def validate_and_clean(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    if "category" not in df.columns:
        df["category"] = "Uncategorized"

    return df
