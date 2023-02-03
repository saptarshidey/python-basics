
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year, odometer_reading=0):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_description(self):
        """Print a neatly formatted descriptive name"""
        print(f"{self.make} - {self.model} - {self.year}".title())

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
           Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given miles to the odometer reading"""
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def get_description(self):
        """Print a neatly formatted statement describting the battery"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range of this battery"""
        if self.battery_size == 75: range = 260
        else: range = 315

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Models aspects of a cara, specific to electric vehicles"""

    def __init__(self, make, model, year, odometer_reading=0):
        """Initialize the attributes of the parent class
           Then initialize specific to an electric car"""
        super().__init__(make, model, year, odometer_reading)
        self.battery = Battery()
