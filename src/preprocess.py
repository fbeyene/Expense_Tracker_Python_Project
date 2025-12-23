import pandas as pd

REQUIRED_COLUMNS = {"date", "description", "amount"}


def validate_and_clean(df):
    """
    Validate and clean transaction data.
    Always reports how many rows were kept or removed.
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    before_rows = len(df)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount"])

    after_rows = len(df)
    removed = before_rows - after_rows

    print(
        f"🧹 Preprocessing complete: "
        f"{after_rows} valid row(s), "
        f"{removed} invalid row(s) removed"
    )

    if "category" not in df.columns:
        df["category"] = "Uncategorized"

    return df

