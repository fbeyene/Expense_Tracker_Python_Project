import csv
import os
from datetime import datetime

"""
budget.py

Handles budget variance evaluation and alert generation.
"""

from typing import Dict, List


def evaluate_variances(
    category_totals: Dict[str, float],
    budgets: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate budget variance per category.

    Variance = actual spend - budget

    Returns
    -------
    dict
        Category → variance
    """
    variances = {}

    for category, actual in category_totals.items():
        budget = budgets.get(category, 0)
        variances[category] = actual - budget

    return variances


def generate_budget_alerts(
    variances: Dict[str, float],
    threshold: float = 0.0
) -> List[str]:
    """
    Generate budget alerts for overspending categories.

    Parameters
    ----------
    variances : dict
        Category → variance
    threshold : float
        Minimum variance to trigger alert

    Returns
    -------
    list
        Human-readable alert messages
    """
    alerts = []

    for category, diff in variances.items():
        if diff > threshold:
            alerts.append(
                f"⚠ {category} is OVER budget by ${diff:.2f}"
            )

    return alerts


def log_budget_alerts(
    variances: dict,
    log_dir: str = "output/audit_logs",
    log_file: str = "budget_alerts.csv"
):
    """
    Log budget overruns to a CSV audit log.

    Parameters
    ----------
    variances : dict
        Category → variance
    """
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, log_file)

    file_exists = os.path.isfile(path)

    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header only once
        if not file_exists:
            writer.writerow(["timestamp", "category", "variance"])

        for category, diff in variances.items():
            if diff > 0:
                writer.writerow([
                    datetime.now().isoformat(),
                    category,
                    round(diff, 2)
                ])