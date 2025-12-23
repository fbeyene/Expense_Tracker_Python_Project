import pandas as pd


def calculate_totals(df: pd.DataFrame):
    """
    Calculate total spending and spending by category.

    Parameters
    ----------
    df : pd.DataFrame
        Transaction data with 'amount' and 'category' columns.

    Returns
    -------
    tuple
        (total_spend, category_totals)
    """
    if df.empty:
        return 0, {}

    total_spend = df["amount"].sum()
    category_totals = df.groupby("category")["amount"].sum().to_dict()

    return total_spend, category_totals


def calculate_variances(category_totals: dict, budgets: dict):
    """
    Calculate variance between actual spending and budget.

    Parameters
    ----------
    category_totals : dict
        Actual spending per category.
    budgets : dict
        Budget per category.

    Returns
    -------
    dict
        Variance per category (actual - budget).
    """
    variances = {}
    for category, actual in category_totals.items():
        budget = budgets.get(category, 0)
        variances[category] = actual - budget
    return variances


def rank_cost_drivers(category_totals: dict):
    """
    Rank categories by total spending.

    Parameters
    ----------
    category_totals : dict

    Returns
    -------
    list
        Sorted list of (category, amount) tuples.
    """
    return sorted(
        category_totals.items(),
        key=lambda x: x[1],
        reverse=True
    )
