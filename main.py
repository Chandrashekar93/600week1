"""
main.py - Entry point for Week 1 Data Exploration, Cleaning, and Feature Engineering Assignment
Author: Chandrashekar
Date: 2025-10-29
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from data_utils import load_synthetic_data, handle_missing_values, detect_and_handle_outliers
from feature_engineering import create_features

def main():
    print("=== Week 1: Data Exploration, Cleaning, and Feature Engineering ===")

    # 1️⃣ Load Dataset
    df = load_synthetic_data()
    print("\nInitial Dataset Sample:")
    print(df.head())

    # 2️⃣ Basic EDA
    print("\n--- Basic Info ---")
    print(df.info())
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # Visualize distributions
    df.hist(bins=20, figsize=(10, 6))
    plt.tight_layout()
    plt.savefig("histograms.png")
    print("\nSaved histograms.png")

    # 3️⃣ Handle Missing Values
    df = handle_missing_values(df)
    print("\nMissing values handled.")

    # 4️⃣ Outlier Detection & Handling
    df = detect_and_handle_outliers(df, ["Age", "AnnualIncome", "SpendingScore"])

    # 5️⃣ Feature Engineering
    df = create_features(df)

    # 6️⃣ Scaling
    scaler = StandardScaler()
    scaled_cols = ["AnnualIncome", "SpendingScore"]
    df[scaled_cols] = scaler.fit_transform(df[scaled_cols])
    print("\nNumeric features scaled using StandardScaler.")

    # 7️⃣ Save cleaned dataset
    df.to_csv("cleaned_customer_data.csv", index=False)
    print("\nSaved cleaned_customer_data.csv")
    print("\nFinal Data Sample:")
    print(df.head())

if __name__ == "__main__":
    main()
