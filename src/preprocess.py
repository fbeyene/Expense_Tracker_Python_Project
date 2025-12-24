import pandas as pd

REQUIRED_COLUMNS = {"date", "description", "amount"}

def validate_and_clean(df):
    """
    Validate and clean the transaction DataFrame.
    Converts 'date' and 'amount' to proper types,
    drops rows with invalid or missing values, and
    fills missing categories.
    """
    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    # Count rows before cleaning
    initial_rows = len(df)

    # Convert types (invalid parsing becomes NaN)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Drop rows with invalid date or amount
    df = df.dropna(subset=["date", "amount"])

    # Count invalid rows removed
    removed_rows = initial_rows - len(df)

    # Fill category if missing
    if "category" not in df.columns:
        df["category"] = "Uncategorized"

    # Print preprocessing summary
    print(f"🧹 Preprocessing complete: {len(df)} valid row(s), {removed_rows} invalid row(s) removed")

    return df




