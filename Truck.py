#Create a Truck object with variables
from HashTable import my_hash


class Truck:
    def __init__(self, truck_number, driver, mileage, speed, current_time, route, current_location, max_packages, current_packages):
        self.truck_number = truck_number
        self.driver = driver
        self.mileage = mileage
        self.speed = speed
        self.current_time = current_time
        self.route = route
        self.current_location = current_location
        self.max_packages = max_packages
        self.current_packages = current_packages

    def add_packages(self, *package_ids):
        for package_id in package_ids:
            package = my_hash.search(package_id)
            self.current_packages.append(package)
            print(f"Package {package_id} added to Truck {self.truck_number}")

truck1 = Truck(1, 1, 18, 8, "08:00 AM", 0, 16, [], [])
truck2 = Truck(2, 2, 18, 8, "08:00 AM", 0, 16, [], [])
truck3 = Truck(3, 0, 18, 8, "08:00 AM", 0, 16, [], [])


truck1.add_packages(4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 19, 20, 29, 30, 31)
truck2.add_packages(1, 3, 18, 34, 36, 37, 38, 40)
truck3.add_packages( 2, 6, 9, 17, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39)

for package in truck1.current_packages:
    print(package)
for package in truck2.current_packages:
    print(package)
for package in truck3.current_packages:
    print(package)