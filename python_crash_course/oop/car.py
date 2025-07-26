class Car:
    def __init__(self, make, model, year):
        """Initialize attributes for car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # This set's a default value

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    ## OR You can use a new method to do the same thing
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't reduce mileage on odometer only increase.")

    def increment_odometer(self, miles):
        """Add a given amount to the odometer"""
        if miles <= 0:
            print("you can decrement you odometer, nice try.")
        self.odometer += miles
        if self.odometer >= 50_000:
            print("Have you considered getting an oil change?")


if __name__ == "__main__":
    new_car = Car("audi", "a4", 2024)

    print(new_car.get_descriptive_name())
    new_car.read_odometer()

    old_car = Car("toyota", "corolla", 1998)
    old_car.odometer = (
        125_000  # to change the default value you can just define it outright.
    )

    print(old_car.get_descriptive_name())
    old_car.read_odometer()

    old_car.update_odometer(212342)
    old_car.read_odometer()

    old_car.update_odometer(234)
