# 📈 Stock Price Predictor using Machine Learning

This project predicts the closing stock price of **Tata Consultancy Services (TCS)** using historical data from **2018 to 2025**. 

---

## 🚀 Project Overview

- 🔍 **Goal**: Predict TCS stock price using historical data
- 🧠 **Models Used**:
  - Linear Regression (Baseline)
  - Random Forest Regressor (Better accuracy)
- 📅 **Data Range**: 2018-01-01 to 2025-07-08
- 📊 **Data Source**: Yahoo Finance via `yfinance` package
- 📓 **Platform**: Jupyter Notebook (Python)

---

## ⚙️ Steps Performed

1. **Data Collection** using `yfinance`
2. **Preprocessing**
   - Removed headers & cleaned columns
   - Handled missing values
   - Converted dates and created `Days` feature
3. **Visualization**
   - Closing price trend (2018–2024)
4. **Modeling**
   - Linear Regression (baseline)
   - Random Forest Regressor (non-linear trends)
5. **Evaluation**
   - R² Score, Mean Squared Error
   - Actual vs Predicted plots

---

## 📉 Results Summary

| Model              | R² Score | MSE         |
|-------------------|----------|-------------|
| Linear Regression | -0.8024  | 186170.57   |
| Random Forest     | -0.6231  | 167650.31   |

> Models struggled due to stock price volatility. Results can be improved using LSTM, ARIMA, or technical indicators.

---

## 💻 Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```
Developed By --Rushabh Kirad