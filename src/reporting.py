def generate_summary(
    total_spend: float,
    score: int,
    alerts: list
) -> str:
    """
    Generate an executive summary including budget alerts.
    """
    summary_lines = [
        "📊 Expense Summary",
        "-" * 18,
        f"Total Spend      : ${total_spend:,.2f}",
        f"Efficiency Score : {score}/100",
    ]

    if alerts:
        summary_lines.append("")
        summary_lines.append("🚨 Budget Alerts Summary")
        summary_lines.append(f"- {len(alerts)} category(ies) over budget")

        # Count severities
        high = sum("[HIGH]" in a for a in alerts)
        medium = sum("[MEDIUM]" in a for a in alerts)
        low = sum("[LOW]" in a for a in alerts)

        if high:
            summary_lines.append(f"  • HIGH severity   : {high}")
        if medium:
            summary_lines.append(f"  • MEDIUM severity : {medium}")
        if low:
            summary_lines.append(f"  • LOW severity    : {low}")
    else:
        summary_lines.append("")
        summary_lines.append("✅ All categories are within budget")

    return "\n".join(summary_lines)




def print_rankings(ranked_costs):
    """
    Print ranked cost drivers.

    Args:
        ranked_costs (list): List of (category, amount) tuples
    """
    print("\n📊 Organized Spending Summary by Category (Top Cost Drivers):")
    print("-------------------------------------------------------------")
    print("\n🔥 Top Cost Drivers")
    print("------------------")

    for i, (category, amount) in enumerate(ranked_costs, start=1):
        print(f"{i}. {category:<15} ${amount:,.2f}")
