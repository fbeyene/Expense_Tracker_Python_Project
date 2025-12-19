import os
import pandas as pd

# Required columns for transaction ingestion
REQUIRED_COLUMNS = {"date", "description", "amount"}


def load_transactions(path: str = "data/transactions.csv") -> pd.DataFrame:
    """
    Load and validate transaction data from a CSV file.

    This function performs the following steps:
    - Checks whether the transaction file exists.
    - Loads transaction data into a pandas DataFrame.
    - Validates that required columns are present.
    - Converts the 'date' column to datetime.
    - Converts the 'amount' column to numeric.
    - Drops invalid or incomplete rows.
    - Returns a clean DataFrame ready for downstream analysis.

    If any errors occur, a friendly warning message is printed and
    an empty DataFrame is returned instead of crashing the program.

    Parameters
    ----------
    path : str, optional
        Relative path to the transaction CSV file.
        Defaults to 'data/transactions.csv'.

    Returns
    -------
    pd.DataFrame
        Cleaned transaction data, or an empty DataFrame if loading fails.
    """

    # Check that the file exists
    if not os.path.exists(path):
        print("⚠ Transaction file not found.")
        return pd.DataFrame()

    try:
        # Load CSV data
        df = pd.read_csv(path)

        # Validate required columns
        missing_columns = REQUIRED_COLUMNS - set(df.columns)
        if missing_columns:
            print(f"⚠ Missing required columns: {', '.join(missing_columns)}")
            return pd.DataFrame()

        # Convert data types
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

        # Remove invalid rows
        df = df.dropna(subset=["date", "amount"])

        print(f"✅ Loaded {len(df)} valid transactions")
        return df

    except Exception as error:
        print(f"⚠ Failed to load transactions: {error}")
        return pd.DataFrame()

