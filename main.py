from src.ingest import load_transactions
from src.preprocess import validate_and_clean
from src.categorize import auto_categorize
from src.analysis import calculate_totals, rank_cost_drivers
from src.budget import evaluate_variances, generate_budget_alerts, log_budget_alerts
from src.scoring import efficiency_score
from src.reporting import generate_summary, print_rankings
from src.config_loader import load_budgets
from src.audit_logger import log_run   # 🔹 STEP 7 import
from src.anomalies import detect_spending_anomalies   # 🔹 NEW (Unusual patterns)

# 🔹 NEW (Interactive CLI features)
from src.interactive import (
    show_menu,
    add_transaction,
    edit_transaction,
    delete_transaction
)


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

    # =============================
    # 🔹 INTERACTIVE TRANSACTION MENU
    # =============================
    while True:
        choice = show_menu()

        if choice == "1":
            df = add_transaction(df)
        elif choice == "2":
            df = edit_transaction(df)
        elif choice == "3":
            df = delete_transaction(df)
        elif choice == "4":
            print("Proceeding to analysis...\n")
            break
        else:
            print("Invalid selection. Please try again.")



    # Load budgets
    budgets = load_budgets()

    # Financial analysis
    total_spend, category_totals = calculate_totals(df)# Calculate budget variances

    # 🔹 STEP: Detect unusual spending patterns
    anomalies = detect_spending_anomalies(
        current_totals=category_totals,
        historical_averages={
            "Fuel": 1400,
            "Maintenance": 570,
            "Insurance": 560
        }
    )

    variances = evaluate_variances(category_totals, budgets)
    alerts = generate_budget_alerts(category_totals, budgets)



    print("\n📉 Budget Variance Report")
    print("------------------------")
    for category, diff in variances.items():
        status = "OVER budget" if diff > 0 else "UNDER budget"
        print(f"{category:<15} ${diff:>8.2f} ({status})")

    # Log alerts to audit file
    log_budget_alerts(category_totals, budgets)

    if alerts:
        print("\n🚨 Budget Alerts")
        print("----------------")
        for alert in alerts:
            print(alert)
            print()  # blank line between alerts
    else:
        print("\n✅ No budget overruns detected")

    if anomalies:
        print("\n🚨 Unusual Spending Alerts")
        print("--------------------------")
        for alert in anomalies:
            print(alert)
            print()  # blank line for readability

    total_budget = sum(budgets.values())
    ranked_costs = rank_cost_drivers(category_totals)

    # Scoring
    score, score_reason = efficiency_score(
        total_spend=total_spend,
        total_budget=total_budget,
        category_variances=variances
    )

    print("\n📊 Efficiency Score")
    print("-------------------")
    print(f"Overall Efficiency Score: {score}/100")
    print(f"Reason: {score_reason}")

    # Reporting
    print(generate_summary(total_spend, score, alerts))
    print_rankings(ranked_costs)

    # 🔹 STEP 7 — Audit Logging
    log_run(
        transactions_count=len(df),
        total_spend=total_spend,
        efficiency_score=score
    )


if __name__ == "__main__":
    main()

