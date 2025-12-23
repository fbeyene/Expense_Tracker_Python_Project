from datetime import datetime
import os


def log_run(
    transactions_count: int,
    total_spend: float,
    efficiency_score: int,
    log_path: str = "output/audit_logs/audit.log"
):
    """
    Append a run summary to the audit log.

    Args:
        transactions_count (int): Number of transactions processed
        total_spend (float): Total spending amount
        efficiency_score (int): Efficiency score (0–100)
        log_path (str): Path to audit log file
    """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{timestamp}] "
        f"Transactions={transactions_count}, "
        f"TotalSpend=${total_spend:,.2f}, "
        f"EfficiencyScore={efficiency_score}\n"
    )

    with open(log_path, "a") as f:
        f.write(log_entry)

