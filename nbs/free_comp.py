import matplotlib.pyplot as plt
from sympy import *
import sympy

class Graph_free_market:
    def __init__(self) -> None:
        pass
        
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
        

    def market_graph(self, supply: str, demand: str, start: int, end: int, step: int, complete = False) -> None:
        """ from sympy import symbols, parse_expr,solve, Eq
        import matplotlib.pyplot as plt """
        

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


    def get_calculate_values(self, expression: str, start: int, end: int, step: int) -> dict:
        #from sympy import symbols, parse_expr,solve, Eq
        value_pairs = {}
        equation_function = self.create_equation_function(expression)
        if equation_function:
            x_values = [i for i in range(start, end, step)]
            for x_val in x_values:
                result = equation_function(x_val)
                value_pairs[x_val] = result
                
               # print(f"For x = {x_val}, the result is {result}")

        else:
            print("Error: Unable to create the equation function.")
        return value_pairs


    def create_equation_function(self, equation_str: str) -> str:
        x = symbols('x')
        
        try:
            equation = parse_expr(equation_str)
            equation_function = lambda x_val: equation.subs(x, x_val)
            return equation_function
        except Exception as e:
            return None


    def get_quantity(self, supply: str, demand: str) -> float:
        x = symbols('x')
        
        # Create the equation from the supply and demand functions
        supply_eq = parse_expr(supply)
        demand_eq = parse_expr(demand)
        
        # Calculate the equilibrium price and quantity
        quantity = max(solve(Eq(supply_eq, demand_eq), x))
        return round(quantity)
    

    def get_price(self, supply: str, demand: str) -> float:
        x, y = symbols('x y')
        
        # Create the equation from the supply and demand functions
        supply_eq = parse_expr(supply)
        demand_eq = parse_expr(demand)

        inverse_supply = solve(supply_eq - y, x)[0]
        inverse_demand = solve(demand_eq - y, x)[0]
        

        price = max(solve(Eq(inverse_supply, inverse_demand), y))
        
        return round(price)

        
    def get_consumer_surplus(self, supply: str, demand: str) -> float:
        x, y = symbols('x y')
        
        # Create the equation from the supply and demand functions
        supply_eq = parse_expr(supply)
        demand_eq = parse_expr(demand)
        
        # Calculate the equilibrium price and quantity
        price = self.get_price(supply, demand)
        quantity = self.get_quantity(supply, demand)
        
        # Define the inverse demand function (price as a function of quantity)
        consumer_surplus = parse_expr(f"{demand}-{price}")
        
        # Calculate consumer surplus
        surplus = sympy.integrate(consumer_surplus, (x, 0, quantity)) 
        
        return round(surplus)
    

    def get_producer_surplus(self, supply: str, demand: str) -> float:
        x, y = symbols('x y')
        
        # Create the equation from the supply and demand functions
        supply_eq = parse_expr(supply)
        demand_eq = parse_expr(demand)
        
        # Calculate the equilibrium price and quantity
        price = self.get_price(supply, demand)
        quantity = self.get_quantity(supply, demand)
        
        # Define the inverse demand function (price as a function of quantity)
        inverse_supply = solve(supply_eq - y, x)[0]

        producer_surplus = parse_expr(f"{quantity}-{inverse_supply}")
        
        # Calculate consumer surplus
        surplus = sympy.integrate(producer_surplus, (y, 0, price)) 
        
        return round(surplus)


    def get_economic_surplus(self, supply: str, demand: str) -> float:
        consumer = self.get_consumer_surplus(supply, demand)
        producer = self.get_producer_surplus(supply, demand)
        economic_surplus = consumer + producer
        return economic_surplus