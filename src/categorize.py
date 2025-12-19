import pandas as pd
import yaml
import os


def load_rules(path="config/rules.yml"):
    """
    Load auto-categorization rules from a YAML file.

    Parameters
    ----------
    path : str
        Path to the YAML file containing category rules.

    Returns
    -------
    dict
        Dictionary mapping categories to keyword lists.
    """
    if not os.path.exists(path):
        print("⚠ Rules file not found. Using default empty rules.")
        return {}

    try:
        with open(path, "r") as file:
            rules = yaml.safe_load(file)
            return rules.get("rules", {})
    except Exception as e:
        print(f"⚠ Error loading rules: {e}")
        return {}


def auto_categorize(df: pd.DataFrame, rules_path="config/rules.yml") -> pd.DataFrame:
    """
    Auto-assign categories to transactions based on rules keywords.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with transactions. Must contain 'description' column.
    rules_path : str
        Path to YAML rules file.

    Returns
    -------
    pd.DataFrame
        DataFrame with an added 'category' column.
    """
    if df.empty:
        return df

    rules = load_rules(rules_path)

    def assign_category(desc: str) -> str:
        desc_lower = str(desc).lower()
        for category, info in rules.items():
            for keyword in info.get("keywords", []):
                if keyword.lower() in desc_lower:
                    return category
        return "Other"  # default if no match

    df["category"] = df["description"].apply(assign_category)
    return df


