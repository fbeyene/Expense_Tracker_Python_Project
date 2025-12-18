KEYWORDS = {
    "fuel": "Fuel",
    "gas": "Fuel",
    "repair": "Maintenance",
    "food": "Food",
    "insurance": "Insurance"
}


def auto_categorize(df):
    for word, category in KEYWORDS.items():
        mask = df["description"].str.lower().str.contains(word, na=False)
        df.loc[mask, "category"] = category
    return df
