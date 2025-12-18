def calculate_totals(df):
    total_spend = df["amount"].sum()
    category_totals = df.groupby("category")["amount"].sum()
    return total_spend, category_totals


def calculate_variances(category_totals, budgets):
    return {
        category: category_totals.get(category, 0) - budgets.get(category, 0)
        for category in budgets
    }


def rank_cost_drivers(category_totals):
    return category_totals.sort_values(ascending=False)

