import pulp


def run_optimization(input_data):
    """
    Run the inventory allocation optimization model.
    This function sets up the problem, defines the decision variables,
    constraints, and objective function, and then solves the model.
    """

    stores, days, demand, holding_cost, shortage_weight, capacity, initial_inventory = (
        input_data[k] for k in [
            'stores',
            'days',
            'demand',
            'holding_cost',
            'shortage_weight',
            'capacity',
            'initial_inventory'
        ]
    )

    # Model
    model = pulp.LpProblem("Inventory_Allocation", pulp.LpMinimize)

    # Decision variables
    x = pulp.LpVariable.dicts("Ship", (stores, days), lowBound=0, cat="Continuous")
    Inv = pulp.LpVariable.dicts("Inventory", (stores, days), lowBound=0, cat="Continuous")
    s = pulp.LpVariable.dicts("Shortage", (stores, days), lowBound=0, cat="Continuous")

    # Objective function: Minimize total cost
    model += pulp.lpSum([
        holding_cost[i] * Inv[i][t] + shortage_weight[i] * s[i][t]
        for i in stores for t in days
    ])

    # Inventory and shortage constraints
    for i in stores:
        for t_index in range(len(days)):
            t = days[t_index]
            if t_index == 0:
                model += Inv[i][t] == initial_inventory[i] + x[i][t] - demand[i, t] + s[i][t], f"FlowBalance_{i}_{t}" # Inventory balance
                model += s[i][t] >= demand[i, t] - initial_inventory[i] - x[i][t], f"Shortage_{i}_{t}" # Shortage constraint
            else:
                t_minus_1 = days[t_index - 1]
                model += Inv[i][t] == Inv[i][t_minus_1] + x[i][t] - demand[i, t] + s[i][t], f"FlowBalance_{i}_{t}" # Inventory balance
                model += s[i][t] >= demand[i, t] - Inv[i][t_minus_1] - x[i][t], f"Shortage_{i}_{t}" # Shortage constraint            

    # Shipping capacity constraint per day
    for t in days:
        model += pulp.lpSum([x[i][t] for i in stores]) <= capacity[t], f"Capacity_{t}"

    # Solve
    model.solve()

    # Output solution
    print("Status:", pulp.LpStatus[model.status])
    print("Total Cost:", pulp.value(model.objective))
    # for i in stores:
    #     for t in days:
    #         print(f"{i}, Day {t}: Ship={x[i][t].varValue}, Inventory={Inv[i][t].varValue}, Shortage={s[i][t].varValue}")

    # Save results
    shipment_decisions = {(i, t): x[i][t].varValue for i in stores for t in days}
    inventory_decisions = {(i, t): Inv[i][t].varValue for i in stores for t in days}
    shortage_decisions = {(i, t): s[i][t].varValue for i in stores for t in days}

    holding_costs = {(i, t): holding_cost[i] * Inv[i][t].varValue for i in stores for t in days}
    shortage_weights = {(i, t): shortage_weight[i] * s[i][t].varValue for i in stores for t in days}

    total_cost = pulp.value(model.objective)

    return {
        'demand': demand,
        'shipment_decisions': shipment_decisions,
        'inventory_decisions': inventory_decisions,
        'shortage_decisions': shortage_decisions,
        'holding_costs': holding_costs,
        'shortage_weights': shortage_weights,
        'total_cost': total_cost
    }
