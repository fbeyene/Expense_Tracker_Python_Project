import os
import pandas as pd

REQUIRED_COLUMNS = {"date", "description", "amount"}


def load_transactions(path: str = "data/transactions.csv") -> pd.DataFrame:
    """
    Load transaction data from a CSV file.

    Responsibilities:
    - Check file existence
    - Load CSV into DataFrame
    - Validate required columns
    - Return raw data for preprocessing

    Returns an empty DataFrame if loading fails.
    """

    if not os.path.exists(path):
        print("⚠ Transaction file not found.")
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)

        missing_columns = REQUIRED_COLUMNS - set(df.columns)
        if missing_columns:
            print(f"⚠ Missing required columns: {', '.join(missing_columns)}")
            return pd.DataFrame()

        print(f"✅ Loaded {len(df)} raw transaction(s)")
        return df

    except Exception as error:
        print(f"⚠ Failed to load transactions: {error}")
        return pd.DataFrame()
