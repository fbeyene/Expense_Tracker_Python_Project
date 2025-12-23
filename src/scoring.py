def efficiency_score(total_spend, total_budget):
    """
    Calculate efficiency score based on spending vs budget.

    Returns a value between 0 and 100.
    """
    if total_budget == 0:
        return 100.0  # No budget means no overspending

    score = 1 - (total_spend / total_budget)
    return round(max(score, 0) * 100, 2)


