from src.ingest import load_transactions
from src.preprocess import validate_and_clean
from src.categorize import auto_categorize
from src.analysis import calculate_totals, calculate_variances, rank_cost_drivers
from src.scoring import efficiency_score
from src.reporting import generate_summary, print_rankings
from src.config_loader import load_budgets
from src.audit_logger import log_run   # 🔹 STEP 7 import


def main():
    # Load and process transactions
    df = load_transactions("data/transactions.csv")
    df = validate_and_clean(df)
    df = auto_categorize(df)

    # Load budgets
    budgets = load_budgets()

    # Financial analysis
    total_spend, category_totals = calculate_totals(df)
    total_budget = sum(budgets.values())
    ranked_costs = rank_cost_drivers(category_totals)

    # Scoring
    score = efficiency_score(total_spend, total_budget)

    # Reporting
    print(generate_summary(total_spend, score))
    print_rankings(ranked_costs)

    # 🔹 STEP 7 — Audit Logging
    log_run(
        transactions_count=len(df),
        total_spend=total_spend,
        efficiency_score=score
    )


if __name__ == "__main__":
    main()

