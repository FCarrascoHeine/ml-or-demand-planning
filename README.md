# 📦 Forecast & Optimize – Demand Planning with ML + OR on AWS

This project demonstrates an end-to-end demand planning pipeline combining machine learning (ML) and operations research (OR), using AWS services where possible.

## 🚀 Overview

The goal is to forecast product demand using a machine learning model (e.g., XGBoost) and then use the forecasted values as inputs to an inventory allocation optimization model. Eventually, the full pipeline will be deployed as a callable REST API on AWS.

## 📊 Data

The project is based on the Rossmann Store Sales dataset from a Kaggle competition. It contains daily sales data for over 1,000 stores across several years, along with associated features such as promotions, holidays, and store metadata. This rich dataset enables realistic demand forecasting by capturing temporal patterns and external drivers of sales.

> ⚠️ **Note:** The dataset in this repository is a **mocked version**. The original dataset can be found here:  
[🔗 Kaggle: Rossmann Store Sales](https://www.kaggle.com/competitions/rossmann-store-sales)

## ✅ Current Status

- ✅ Data preprocessing complete  
- ✅ ML pipeline implemented in Jupyter notebooks (XGBoost-based forecasting)  
- ⏳ Next step: define and solve the OR optimization model (e.g., using PuLP or SciPy)

## 🛠️ Tools Used

- Python, Jupyter
- XGBoost
- (Soon) PuLP or SciPy for optimization
- (Planned) AWS SageMaker, S3, Lambda for deployment

## 📁 Structure

```
.
├── data/                # Mocked data samples; include real data in this folder
├── notebooks/           # ML pipeline and preprocessing (Jupyter notebooks)
├── results/             # Results are saved here
├── src/                 # Planned: scripts for OR model and deployment logic
├── README.md
```

## 📌 Next Steps

- Implement and test the OR model locally
- Define ML → OR handoff interface
- Begin migrating components to AWS

---