# define class
class Vehicle:
    def __init__(self, name, mileage, price):
        self.name = name
        self.mileage = mileage
        self.price = price
        self.speed = 0.0

    def get_name(self):
        return self.name

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price

    def get_speed(self):
        return self.speed

    def start(self, speed):
        if (speed > 0): self.speed = speed
        print(f"{self.get_name()} started. Now it's running at {self.get_speed()} miles/hr")

    def stop(self):
        self.speed = 0.0
        print(f"{self.get_name()} stopped")

    def get_info(self):
        return f"Name: {self.get_name()}, Mileage: {self.get_mileage()}, Price: {self.get_price()}, Speed: {self.get_speed()}"

class Scooter(Vehicle):
    def __init__(self, name, mileage, price, battery):
        super().__init__(name, mileage, price)
        self.battery = battery

    def is_battery_operated(self):
        return self.battery

    def get_info(self):
        return f"{super().get_info()}, Battery Operated: {self.is_battery_operated()}"

class Car(Vehicle):
    def __init__(self, name, mileage, price, automatic):
        super().__init__(name, mileage, price)
        self.automatic = automatic

    def is_automatic(self):
        return self.automatic

    def get_info(self):
        return f"{super().get_info()}, Automatic: {self.is_automatic()}"


# create objects
vespa = Scooter("Vespa", 40, 50000, False)
ather = Scooter("Ather", 50, 100000, True)
hyundai = Car("Verna", 15, 1500000, False)
honda = Car("City", 14, 2000000, True)

print(vespa.get_info())
print(ather.get_info())
print(hyundai.get_info())
print(honda.get_info())

vespa.start(30)
ather.start(30)
hyundai.start(30)
honda.start(30)

print(vespa.get_info())
print(ather.get_info())
print(hyundai.get_info())
print(honda.get_info())

vespa.stop()
ather.stop()
hyundai.stop()
honda.stop()

print(vespa.get_info())
print(ather.get_info())
print(hyundai.get_info())
print(honda.get_info())
