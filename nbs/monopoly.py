import matplotlib.pyplot as plt
from sympy import *
import sympy
from free_comp import Graph_free_market
class Graph_monopoly(Graph_free_market):
    def __init__(self) -> None:
        super().__init__()
        
    
    def market_graph(self, supply: str, demand: str, start: int, end: int, step: int, complete = False, is_tot_cost = False) -> None:
        x = symbols('x')
        
        if is_tot_cost == True:
            supply_parsed = parse_expr(supply)
            marginal_cost = diff(supply_parsed, x)
        
        demand_parsed = parse_expr(demand)
        marginal_revenue = diff(demand_parsed, x)
        
        
        
        supply, demand =str(marginal_cost), str(marginal_revenue)
        
        
        
        price = self.get_price(supply, demand)
        quantity = self.get_quantity(supply, demand)

        supply = self.get_calculate_values(supply, start, end, step)
        demand = self.get_calculate_values(demand, start, end, step)

        if complete == True:
            plt.plot([i for i in range(0, round(quantity) + 1)], [price for i in range(0, round(quantity) + 1)],
                     linestyle = "dashed", label = f"Price*: {price}")
            plt.plot([quantity for i in range(0, round(price) + 1 )], [i for i in range(0,round(price) + 1)],
                     linestyle = "dashed", label = f"Quantity*: {quantity}")


     
        plt.plot(supply.keys(),supply.values(), label = "Supply") 
        plt.plot(demand.keys(),demand.values(), label = "Demand") 

        

        plt.xlabel("Quantity")
        plt.ylabel("Price")

        plt.legend() 
        plt.show()