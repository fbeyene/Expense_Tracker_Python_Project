"""
interactive.py

Provides simple CLI-based interaction for modifying expense data.
"""

import pandas as pd
from datetime import datetime

DEFAULT_DESCRIPTIONS = {
    "Fuel": "Fuel expense",
    "Food": "Food purchase",
    "Maintenance": "Vehicle maintenance",
    "Insurance": "Insurance payment",
    "Other": "General expense"
}


def show_menu() -> str:
    print("\n📋 Expense Tracker Menu")
    print("----------------------")
    print("1. Add Transaction")
    print("2. Edit Transaction")
    print("3. Delete Transaction")
    print("4. Continue to Analysis")
    print("5. Exit")

    return input("Enter your choice (1–5): ").strip()


def add_transaction(df):
    print("\n➕ Add a New Transaction")

    category = input("Category: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()

    # Safe amount input
    while True:
        amount_input = input("Amount: ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value (e.g., 25.50).")

    # ✅ Use default description if available
    description = DEFAULT_DESCRIPTIONS.get(category, f"{category} expense")

    new_row = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    df = df._append(new_row, ignore_index=True)
    print("✅ Transaction added successfully\n")  # Blank line for readability

    return df


def edit_transaction(df: pd.DataFrame) -> pd.DataFrame:
    print("\n✏️ Edit Transaction")

    print(df[["date", "category", "description", "amount"]])
    try:
        idx = int(input("Enter row index to edit: "))
    except ValueError:
        print("❌ Invalid index input.")
        return df

    if idx not in df.index:
        print("❌ Invalid index.")
        return df

    # Edit Category
    new_category = input(f"New Category (current: {df.at[idx, 'category']}): ").strip()
    if new_category:
        df.at[idx, "category"] = new_category
        # Only set default description if the user leaves description blank
        new_description = input(f"New Description (leave blank to use default for {new_category}): ").strip()
        if new_description:
            df.at[idx, "description"] = new_description
        else:
            # Auto-fill based on category
            df.at[idx, "description"] = DEFAULT_DESCRIPTIONS.get(new_category, f"{new_category} expense")

    # Edit Amount
    while True:
        new_amount_input = input(f"New Amount (current: {df.at[idx, 'amount']}): ").strip()
        if not new_amount_input:
            break  # Keep existing
        try:
            new_amount = float(new_amount_input)
            if new_amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            df.at[idx, "amount"] = new_amount
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value (e.g., 25.50).")

    print("✅ Transaction updated successfully\n")  # Blank line for readability
    return df


def delete_transaction(df: pd.DataFrame) -> pd.DataFrame:
    print("\n🗑 Delete Transaction")

    print(df[["date", "category", "description", "amount"]])
    idx = int(input("Enter row index to delete: "))

    if idx not in df.index:
        print("❌ Invalid index.")
        return df

    df = df.drop(index=idx).reset_index(drop=True)
    print("✅ Transaction deleted.")

    return df