import pandas as pd

from pathlib import Path

def create_input():
    """
    Creates the input data for the optimization problem.
    This function defines the sets, parameters, and initial inventory.
    It returns a dictionary containing all necessary inputs.
    """
    root = Path.cwd()

    test_df = pd.read_csv(root/'data'/'test.csv')
    predictions_df = pd.read_csv(root/'results'/'predictions.csv')
    input_df = test_df.merge(predictions_df, how='left', on='Id')
    
    # Sets
    stores = ['Store_1', 'Store_2']
    days = list(range(1, 4))  # Days 1 to 3

    # Parameters (example values — replace with actual data)
    demand = {(i, t): 20 for i in stores for t in days}       # demand d_it
    holding_cost = {i: 1.0 for i in stores}                   # holding cost h_i
    shortage_weight = {i: 5.0 for i in stores}                # shortage weight w_i
    capacity = {t: 50 for t in days}                          # warehouse capacity C_t
    initial_inventory = {i: 0 for i in stores}                # initial inventory I_i0

    return {
        'stores': stores,
        'days': days,
        'demand': demand,
        'holding_cost': holding_cost,
        'shortage_weight': shortage_weight,
        'capacity': capacity,
        'initial_inventory': initial_inventory
    }