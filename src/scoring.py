def efficiency_score(total_spend, total_budget):
    if total_budget == 0:
        return 0

    ratio = total_spend / total_budget

    if ratio <= 1:
        return 100
    elif ratio <= 1.2:
        return 75
    elif ratio <= 1.5:
        return 50
    return 25
