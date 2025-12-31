"""
anomalies.py

Detects unusual spending patterns by comparing current totals
against historical averages.
"""

from typing import Dict, List


def detect_spending_anomalies(
    current_totals: Dict[str, float],
    historical_averages: Dict[str, float],
    threshold_pct: float = 0.30
) -> List[str]:
    """
    Identify categories where spending is unusually high.

    An anomaly is flagged when:
        (current - historical_average) / historical_average >= threshold_pct
    """
    alerts: List[str] = []

    for category, current in current_totals.items():
        avg = historical_averages.get(category)

        # Skip categories without historical data
        if avg is None or avg <= 0:
            continue

        increase_pct = (current - avg) / avg

        if increase_pct >= threshold_pct:
            alert = (
                "🚨 Unusual Spending Detected:\n"
                f"Category: {category}\n"
                f"Current Spend: ${current:,.2f}\n"
                f"Historical Average: ${avg:,.2f}\n"
                f"This month's spend is {increase_pct:.0%} higher than average."
            )
            alerts.append(alert)

    return alerts