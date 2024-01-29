from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# can't get it to work, seems it does not recognize ElectricCar. mst car.py, line 46 
#in __init__ self.battery = Battery()
# NameError: name 'Battery' is not defined

