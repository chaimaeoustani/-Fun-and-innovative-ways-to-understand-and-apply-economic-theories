class Market:
    def __init__(self, supply_list, demand_list):
        self.supply_list = supply_list
        self.demand_list = demand_list
        self.price = 1.0
        self.day = 0

    def update_price(self):
        if self.demand > self.supply:
            self.price += 0.1
        elif self.demand < self.supply:
            self.price -= 0.1
        self.price = round(self.price, 2)

    def simulate_day(self):
        self.demand = self.demand_list[self.day]
        self.supply = self.supply_list[self.day]
        self.update_price()
        self.day += 1

supply_data = [100, 120, 80, 150, 130, 90, 110, 140, 70, 100]
demand_data = [110, 100, 130, 90, 120, 80, 140, 70, 150, 100]

market = Market(supply_data, demand_data)

for i in range(10):
    market.simulate_day()
    print(f"Day {i+1}: Price is {market.price} with supply {market.supply} and demand {market.demand}")
