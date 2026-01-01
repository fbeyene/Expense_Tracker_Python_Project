from typing import Dict, Tuple, List


def efficiency_score(
    total_spend: float,
    total_budget: float,
    category_variances: Dict[str, float]
) -> Tuple[int, str]:
    """
    Calculate an efficiency score and provide a clear explanation.

    Score is based on how closely actual spend aligns with budget.
    """
    if total_budget <= 0:
        return 0, "No budget defined; efficiency score unavailable."

    # Base score calculation
    utilization_ratio = total_spend / total_budget
    score = max(0, int(100 - abs(utilization_ratio - 1) * 100))

    # Identify drivers
    overruns = [cat for cat, var in category_variances.items() if var > 0]
    under_budget = [cat for cat, var in category_variances.items() if var <= 0]

    # Build explanation
    if overruns and under_budget:
        explanation = (
            f"High overruns in {', '.join(overruns)} offset "
            f"strong cost control in {', '.join(under_budget)}."
        )
    elif overruns:
        explanation = f"Overspending in {', '.join(overruns)} reduced efficiency."
    else:
        explanation = "Spending remained within budget across all categories."

    return score, explanation


