# Week 1 Assignment: Data Exploration, Cleaning, and Feature Engineering

### Author
Chandrashekar
**Date:** October 29, 2025  

---

## 🎯 Objective
Perform exploratory data analysis, clean missing and outlier values, and engineer useful features using Python in Visual Studio Code.

---

## 🧩 Dataset
A **synthetic customer transaction dataset** generated programmatically.  
Contains:
- `CustomerID`
- `Gender`
- `Age`
- `AnnualIncome`
- `SpendingScore`

**Synthetic Data Parameters:**
- `n = 200 samples`
- `Age ~ Normal(40, 12)`
- `AnnualIncome ~ Normal(60000, 15000)`
- `SpendingScore ∈ [1, 100]`

---

## 🧪 Steps and Decisions
1. **EDA:** Summary statistics, histograms for numeric columns.
2. **Missing Values:** Median imputation for Age, Mean imputation for Income.
3. **Outliers:** Capped using IQR method.
4. **Feature Engineering:**
   - `IncomePerAge`: Ratio-based feature for spending capacity.
   - `SpendingCategory`: Binned spending levels.
5. **Scaling:** StandardScaler for numeric variables to normalize magnitude.

---

## 🛠️ How to Run
1. Clone repo and activate virtual environment:
   ```bash
   git clone <your-repo-url>
   cd week1-data-exploration
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python src/main.py
