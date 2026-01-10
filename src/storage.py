import pandas as pd

def save_transactions(df, file_path="data/transactions.csv"):
    """
    Persist transactions to CSV.
    """
    df.to_csv(file_path, index=False)
    print("💾 Changes saved successfully.")