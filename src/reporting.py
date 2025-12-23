def generate_summary(total_spend: float, score: int) -> str:
    """
    Generate a formatted summary of spending efficiency.

    Args:
        total_spend (float): Total amount spent
        score (int): Efficiency score (0–100)

    Returns:
        str: Summary text
    """
    return (
        f"\n📊 Expense Summary\n"
        f"------------------\n"
        f"Total Spend      : ${total_spend:,.2f}\n"
        f"Efficiency Score : {score}/100\n"
    )


def print_rankings(ranked_costs):
    """
    Print ranked cost drivers.

    Args:
        ranked_costs (list): List of (category, amount) tuples
    """
    print("\n🔥 Top Cost Drivers")
    print("------------------")

    for i, (category, amount) in enumerate(ranked_costs, start=1):
        print(f"{i}. {category:<15} ${amount:,.2f}")
