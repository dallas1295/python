from car import Car


class ElectricCar(Car):
    """Extend the Car class to be specific to Electirc Cars"""

    def __init__(self, make, model, year):
        """Initialize parent class properties"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement for battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """E/V's don't use gasoline"""
        print("This car doesn't have a gas tank")


## only run the additional code when the file is being ran by itself
if __name__ == "__main__":

    my_leaf = ElectricCar("nissan", "leaf", 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.describe_battery()
    my_leaf.fill_gas_tank()
