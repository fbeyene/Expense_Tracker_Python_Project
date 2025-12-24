from src.ingest import load_transactions
from src.preprocess import validate_and_clean
from src.categorize import auto_categorize
from src.analysis import calculate_totals, rank_cost_drivers
from src.budget import evaluate_variances, generate_budget_alerts, log_budget_alerts
from src.scoring import efficiency_score
from src.reporting import generate_summary, print_rankings
from src.config_loader import load_budgets
from src.audit_logger import log_run   # 🔹 STEP 7 import


import os

def main():
    # -----------------------------
    # DEBUG: Verify working directory and file existence
    # -----------------------------
    print("DEBUG: Current working directory =", os.getcwd())
    print("DEBUG: Absolute path being used:", os.path.abspath("data/transactions.csv"))
    print("DEBUG: Does file exist?",
          os.path.exists("data/transactions.csv"))
    # -----------------------------
    # Load and process transactions
    df = load_transactions("data/transactions.csv")

    print("DEBUG: Rows loaded =", len(df))
    print("DEBUG: Last 10 rows:")
    print(df.tail(10)) # Show last 10 rows

    df = validate_and_clean(df)
    df = auto_categorize(df)

    # Load budgets
    budgets = load_budgets()

    # Financial analysis
    total_spend, category_totals = calculate_totals(df)# Calculate budget variances

    variances = evaluate_variances(category_totals, budgets)
    alerts = generate_budget_alerts(variances)

    print("\n📉 Budget Variance Report")
    print("------------------------")
    for category, diff in variances.items():
        status = "OVER budget" if diff > 0 else "UNDER budget"
        print(f"{category:<15} ${diff:>8.2f} ({status})")

    # Log alerts to audit file
    log_budget_alerts(variances)

    if alerts:
        print("\n🚨 Budget Alerts")
        print("----------------")
        for alert in alerts:
            print(alert)
    else:
        print("\n✅ No budget overruns detected")

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

