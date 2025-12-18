import pandas as pd


def load_transactions(path):
    try:
        df = pd.read_csv(path)
        print(f"✅ Loaded {len(df)} transactions")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load transactions: {e}")
