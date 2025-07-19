import random

import pandas as pd

from constants import CAPACITY_FRACTION, HOLDING_SHORTAGE_RATIO, INITIAL_INVENTORY
from pathlib import Path

# Reproducibility
random.seed(42)

def create_input():
    """
    Creates the input data for the optimization problem.
    This function defines the sets, parameters, and initial inventory.
    It returns a dictionary containing all necessary inputs.

    Assumptions:
    - Deliveries can be made daily, even when a store is closed.
    """
    root = Path.cwd()

    test_df = pd.read_csv(root/'data'/'test.csv')
    predictions_df = pd.read_csv(root/'results'/'predictions.csv')
    input_df = test_df.merge(predictions_df, how='left', on='Id')
    input_df['Date'] = pd.to_datetime(input_df['Date'])
    sales_dict = input_df.set_index(['Store', 'Date'])['Sales'].to_dict()

    # Sets
    stores = sorted(input_df['Store'].unique().tolist())
    days = list(
        pd.date_range(start=input_df['Date'].min(), end=input_df['Date'].max(), freq='D')
    )

    # Optimization model parameters - Available values   
    demand = {(i, t): sales_dict.get((i, t), 0) for i in stores for t in days}    # demand d_it
    
    # Optimization model parameters - Randomly or arbitrarily generated values
    holding_cost = {i: HOLDING_SHORTAGE_RATIO * random.random() for i in stores}  # holding cost h_i
    shortage_penalty = {i: random.random() for i in stores}                       # shortage penalty w_i
    
    max_demand = max(sum(demand[i, t] for i in stores) for t in days)
    capacity = {t: CAPACITY_FRACTION*max_demand for t in days}                    # warehouse capacity C_t
    
    initial_inventory = {i: INITIAL_INVENTORY for i in stores}                    # initial inventory I_i0

    return {
        'stores': stores,
        'days': days,
        'demand': demand,
        'holding_cost': holding_cost,
        'shortage_penalty': shortage_penalty,
        'capacity': capacity,
        'initial_inventory': initial_inventory
    }
