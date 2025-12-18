from src.ingest import load_transactions
from src.preprocess import validate_and_clean
from src.categorize import auto_categorize
from src.analysis import calculate_totals, calculate_variances, rank_cost_drivers
from src.scoring import efficiency_score
from src.reporting import generate_summary, print_rankings
from src.config_loader import load_budgets


def main():
    df = load_transactions("data/transactions.csv")
    df = validate_and_clean(df)
    df = auto_categorize(df)

    budgets = load_budgets()
    total_spend, category_totals = calculate_totals(df)

    total_budget = sum(budgets.values())
    ranked_costs = rank_cost_drivers(category_totals)

    score = efficiency_score(total_spend, total_budget)

    print(generate_summary(total_spend, score))
    print_rankings(ranked_costs)


if __name__ == "__main__":
    main()

