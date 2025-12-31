"""
analysis.py

Performs core financial analysis and aggregation.
"""

import pandas as pd
from typing import Dict, Tuple, List, cast



def calculate_totals(df: pd.DataFrame) -> Tuple[float, Dict[str, float]]:
    """
    Calculate total spending and spending by category.

    Parameters
    ----------
    df : pd.DataFrame
        Transaction data with 'amount' and 'category' columns.

    Returns
    -------
    Tuple[float, Dict[str, float]]
        (total_spend, category_totals)
    """
    if df.empty:
        return 0.0, {}

    total_spend = float(df["amount"].sum())

    category_totals = cast(
        Dict[str, float],
        df.groupby("category")["amount"]
        .sum()
        .to_dict()
    )

    return total_spend, category_totals


def rank_cost_drivers(category_totals: Dict[str, float]) -> List[Tuple[str, float]]:
    """
    Rank categories by total spending (highest to lowest).

    Parameters
    ----------
    category_totals : Dict[str, float]

    Returns
    -------
    List[Tuple[str, float]]
        Sorted list of (category, amount) tuples.
    """
    return sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )