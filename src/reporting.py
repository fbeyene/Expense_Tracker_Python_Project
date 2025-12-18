def generate_summary(total_spend, score):
    return (
        f"Executive Summary\n"
        f"-----------------\n"
        f"Total Spend: ${total_spend:,.2f}\n"
        f"Efficiency Score: {score}/100\n"
    )


def print_rankings(ranked_costs):
    print("\nTop Cost Drivers:")
    for category, amount in ranked_costs.items():
        print(f"{category}: ${amount:,.2f}")
