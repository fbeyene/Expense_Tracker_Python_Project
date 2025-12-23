def efficiency_score(total_spend: float, total_budget: float) -> int:
    """
    Calculate an efficiency score based on spending vs budget.

    Score is capped at 100.
    A score below 100 means overspending.
    A score of 100 means on or under budget.

    Args:
        total_spend (float): Total amount spent
        total_budget (float): Total budgeted amount

    Returns:
        int: Efficiency score (0–100)
    """
    if total_budget <= 0:
        return 0

    score = (total_budget / total_spend) * 100

    return min(int(round(score)), 100)

