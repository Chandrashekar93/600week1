"""
data_utils.py - Dataset loading, cleaning, and outlier handling utilities
"""

import pandas as pd
import numpy as np

def load_synthetic_data(seed=42):
    np.random.seed(seed)
    n = 200
    data = {
        "CustomerID": range(1, n + 1),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Age": np.random.normal(40, 12, n).astype(int),
        "AnnualIncome": np.random.normal(60000, 15000, n).astype(int),
        "SpendingScore": np.random.randint(1, 100, n)
    }

    df = pd.DataFrame(data)

    # Add some missing values
    df.loc[np.random.choice(df.index, 10, replace=False), "Age"] = np.nan
    df.loc[np.random.choice(df.index, 8, replace=False), "AnnualIncome"] = np.nan
    return df

def handle_missing_values(df):
    df["Age"].fillna(df["Age"].median(), inplace=True)
    df["AnnualIncome"].fillna(df["AnnualIncome"].mean(), inplace=True)
    return df

def detect_and_handle_outliers(df, cols):
    for col in cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        # Cap outliers
        df[col] = df[col].clip(lower, upper)
    return df
