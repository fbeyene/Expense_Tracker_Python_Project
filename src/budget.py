import csv
import os
from datetime import datetime
from typing import Dict, List

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
    category_totals: Dict[str, float],
    budgets: Dict[str, float]
) -> List[str]:
    """
    Generate detailed budget alerts.

    Variance is calculated as:
        Actual Spend - Budget

    Positive variance indicates overspending.
    Negative variance indicates underspending.
    """
    alerts = []

    for category, actual in category_totals.items():
        budget = budgets.get(category, 0.0)

        # Skip categories with no defined budget
        if budget <= 0:
            continue

        variance = actual - budget

        if variance > 0:
            alert = (
                "⚠ Budget Alert:\n"
                f"Category: {category}\n"
                f"Budget: ${budget:,.2f}\n"
                f"Actual Spend: ${actual:,.2f}\n"
                f"Over Budget Amount: ${variance:,.2f}"
            )
            alerts.append(alert)

    return alerts



def log_budget_alerts(
    category_totals: dict,
    budgets: dict,
    log_dir: str = "output/audit_logs",
    log_file: str = "budget_alerts.csv"
):
    """
    Log budget overruns with severity to a CSV audit log.
    """
    import csv
    import os
    from datetime import datetime

    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, log_file)

    file_exists = os.path.isfile(path)

    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "category", "variance", "severity"])

        for category, actual in category_totals.items():
            budget = budgets.get(category, 0)
            diff = actual - budget

            if diff > 0:
                severity = determine_severity(actual, budget)
                writer.writerow([
                    datetime.now().isoformat(),
                    category,
                    round(diff, 2),
                    severity
                ])



def determine_severity(actual: float, budget: float) -> str:
    """
    Determine alert severity based on overspend percentage.
    """
    if budget <= 0:
        return "HIGH"

    overspend_pct = (actual - budget) / budget

    if overspend_pct <= 0.10:
        return "LOW"
    elif overspend_pct <= 0.25:
        return "MEDIUM"
    else:
        return "HIGH"
