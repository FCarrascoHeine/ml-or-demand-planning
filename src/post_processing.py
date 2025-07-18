import pandas as pd

from pathlib import Path
import json

root = Path.cwd()

def post_processing(output_data):
    """
    Post-processes the output data from the optimization model.
    """
    
    demand_df = dict_to_df(output_data['demand'], ['Store', 'Date', 'Sales'])
    shipment_decisions_df = dict_to_df(output_data['shipment_decisions'], ['Store', 'Date', 'Shipment'])
    inventory_decisions_df = dict_to_df(output_data['inventory_decisions'], ['Store', 'Date', 'Inventory'])
    shortage_decisions_df = dict_to_df(output_data['shortage_decisions'], ['Store', 'Date', 'Shortage'])
    holding_costs_df = dict_to_df(output_data['holding_costs'], ['Store', 'Date', 'HoldingCost'])
    shortage_weights_df = dict_to_df(output_data['shortage_weights'], ['Store', 'Date', 'ShortageWeight'])

    # Save costs
    costs = {
        "total_cost": output_data['total_cost'],
    }
    with open(root/'results'/'total_cost.json', 'w') as f:
        json.dump(costs, f, indent=4)

    # Save DataFrames to CSV files
    demand_df.to_csv(root/'results'/'demand.csv', index=False)
    shipment_decisions_df.to_csv(root/'results'/'shipment_decisions.csv', index=False)
    inventory_decisions_df.to_csv(root/'results'/'inventory_decisions.csv', index=False)
    shortage_decisions_df.to_csv(root/'results'/'shortage_decisions.csv', index=False)
    holding_costs_df.to_csv(root/'results'/'holding_costs.csv', index=False)
    shortage_weights_df.to_csv(root/'results'/'shortage_weights.csv', index=False)


def dict_to_df(my_dict, columns):
    return pd.DataFrame(
        [(i, t, value) for (i, t), value in my_dict.items()],
        columns=columns
    )
