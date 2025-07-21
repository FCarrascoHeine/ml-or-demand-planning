# ⚙️ Forecast & Optimize – Demand Planning with ML + OR

This project demonstrates an end-to-end demand planning pipeline combining machine learning (ML) and operations research (OR).

## 🚀 Overview

The goal is to forecast product demand using a machine learning model and then use the forecasted values as inputs to an inventory allocation optimization model.

## 📊 Data

The project is based on the Rossmann Store Sales dataset from a Kaggle competition. It contains daily sales data for over 1,000 stores across several years, along with associated features such as promotions, holidays, and store metadata. This rich dataset enables realistic demand forecasting by capturing temporal patterns and external drivers of sales.

> ⚠️ **Note:** The dataset in this repository is a **mocked version**. The original dataset can be found here:  
[🔗 Kaggle: Rossmann Store Sales](https://www.kaggle.com/competitions/rossmann-store-sales)

## ✅ Current Status

- ✅ Data preprocessing complete  
- ✅ ML pipeline implemented in Jupyter notebooks (XGBoost-based forecasting) 
- ✅ Define and solve the OR optimization model using PuLP

## 🛠️ Tools Used

- Python, Jupyter
- XGBoost for forecasting
- PuLP for optimization

## 📁 Structure

```
.
├── data/                # Mocked data samples; include real data in this folder
├── notebooks/           # ML pipeline, preprocessing, and visualization of final results (Jupyter notebooks)
├── results/             # Results are saved here
├── src/                 # Scripts for OR model
├── .gitignore
├── README.md
├── requirements.txt
```

## ☁️ Forecasting Approach

We use historical sales data to train an XGBoost regression model for demand forecasting. Model hyperparameters are selected using grid search and cross-validation to ensure robust and accurate predictions.

## 📦 Inventory Allocation Optimization Model

This model is formulated as a linear program using PuLP to optimize inventory allocation across multiple stores and days.

### Simplifying assumptions

- We interpret past sales data as demand.
- Deliveries can take place on any day of the planning horizon (even if stores are closed). Each day, only one delivery to each store is possible, though.

### Objective Function

Minimize the total cost, which is the sum of holding costs and shortage penalties across all stores and days:

```
Minimize:
    sum_{i in stores} sum_{t in days} [ holding_cost[i] * Inventory[i, t] + shortage_penalty[i] * Shortage[i, t] ]
```

### Decision Variables

- **Ship[i, t]**: Quantity shipped to store `i` on day `t` (continuous, ≥ 0)
- **Inventory[i, t]**: Inventory at store `i` at the end of day `t` (continuous, ≥ 0)
- **Shortage[i, t]**: Shortage at store `i` on day `t` (continuous, ≥ 0)

### Parameters

- `stores`: List of store identifiers
- `days`: List of time periods (days)
- `demand[i, t]`: Demand at store `i` on day `t`
- `holding_cost[i]`: Per-unit holding cost for store `i`
- `shortage_penalty[i]`: Per-unit shortage penalty for store `i`
- `capacity[t]`: Total shipping capacity available on day `t`
- `initial_inventory[i]`: Initial inventory at store `i`

### Constraints

1. **Inventory Balance (Flow Balance):**
      ```
      Inventory[i, t] = Inventory[i, t-1] + Ship[i, t] - demand[i, t] + Shortage[i, t]
      ```

2. **Shortage Constraints:**
      ```
      Shortage[i, t] >= demand[i, t] - Inventory[i, t-1] - Ship[i, t]
      ```

3. **Shipping Capacity per Day:**
    ```
    sum_{i in stores} Ship[i, t] <= capacity[t]   for all t in days
    ```

This model determines the optimal shipping, inventory, and shortage levels to minimize total costs while satisfying balance and capacity constraints.


## 📌 Next Steps

- Think of potential extensions and improvements
- Deployment?

---
