from cars import Car, ElectricCar, Battery

my_beetle = Car('volkswagen', 'beetle', 2019)
my_tesla = ElectricCar('tesla', 'model s', 2020)

my_beetle.get_description()
my_beetle.read_odometer()
my_beetle.increment_odometer(100)
my_beetle.update_odometer(80)
my_beetle.read_odometer()

print()

my_tesla.get_description()
my_tesla.read_odometer()
my_tesla.update_odometer(150)
my_tesla.read_odometer()
my_tesla.battery.get_description()
my_tesla.battery.get_range()
