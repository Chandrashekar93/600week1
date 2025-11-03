"""
feature_engineering.py - Feature creation and transformation
"""

import pandas as pd

def create_features(df):
    # Feature 1: Income per Age
    df["IncomePerAge"] = (df["AnnualIncome"] / df["Age"]).replace([float("inf"), -float("inf")], 0)

    # Feature 2: Spending Category (High/Medium/Low)
    df["SpendingCategory"] = pd.cut(
        df["SpendingScore"],
        bins=[0, 40, 70, 100],
        labels=["Low", "Medium", "High"]
    )
    return df
