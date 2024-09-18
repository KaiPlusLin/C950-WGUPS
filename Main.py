# C950 Task 2- Kaitlin Carleton 007899571

import csv
from datetime import timedelta, datetime
from os import close
from AddressData import address_list, get_address_index
from DistanceData import distance_list
from HashTable import ChainingHashTable
from Package import Package
from Truck import Truck


def distance_between(address1, address2):
    index2 = get_address_index(address1)
    index1 = get_address_index(address2)

    distance = float(distance_list[index1][index2])

    return distance


my_hash = ChainingHashTable()

with open('CSV files/packageCSV.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        package = Package(
            id=int(row['package_number']),
            address=row['address'],
            city=row['city'],
            state=row['state'],
            zip_code=row['zip_code'],
            delivery_deadline=row['delivery_deadline'],
            weight=int(row['weight']),
            special_notes=row['special_notes']
        )
        my_hash.insert(package.id, package)

#function using truck as argument
def deliver_packages(truck):

#set truck as enroute
    for package_id in truck.current_packages:
        package = my_hash.search(package_id)
        if package:
            package.delivery_status = "ENROUTE"
            package.truck_number = truck.truck_number
            my_hash.insert(package.id, package)


    #loop checking for undelivered packages
    while len(truck.current_packages) > 0:
        #initialize variables
        min_distance = 2000  # miles
        closest_package = None

        #iterate over each package_id
        for package_id in truck.current_packages:
            #search for package
            package = my_hash.search(package_id)
            #looks for current location
            truck_location = truck.current_location
            #looks for package delivery address
            package_address = package.address
            #uses distance_between function
            distance = distance_between(truck_location, package_address)

            #check if there's a closer package then the current
            if distance < min_distance:
                min_distance = distance
                closest_package = package


        #updates trucks mileage and time
        truck.mileage += min_distance
        truck.current_time += timedelta(hours=min_distance / 18)
        #set delivery time
        closest_package.delivery_time = truck.current_time
        closest_package.departure_time = truck.departure_time
        closest_package.delivery_status = "DELIVERED"
        #update truck's location and remove package from list
        truck.location = closest_package.address
        truck.current_packages.remove(closest_package.id)
        my_hash.insert(closest_package.id, closest_package)


    return truck.mileage




truck1 = Truck(1, [1, 6, 13, 14, 15, 16, 19, 20, 21, 30, 34, 39] ,timedelta(hours=8))
truck2 = Truck(2, [2, 3, 4, 5, 7, 11, 18, 27, 29, 33, 35, 36, 38], timedelta(hours=8))
truck3 = Truck(3, [8, 9, 10, 12, 17, 22, 23, 24, 25, 26, 28, 31, 32, 37, 40], timedelta(hours=9, minutes=5))


deliver_packages(truck1)
deliver_packages(truck2)

total = truck1.mileage + truck2.mileage + truck3.mileage

print(f"Truck 1 mileage: {truck1.mileage:.2f}")
print(f"Truck 2 mileage: {truck2.mileage:.2f}")

if len(truck1.current_packages) == 0 or len(truck2.current_packages) == 0:
    deliver_packages(truck3)

print(f"Truck 3 mileage: {truck3.mileage:.2f}")
print(f"Total = {total:.2f}")

# Console
while True:
    print("*" * 60)
    print("1.  List all packages and statuses")
    print("2.  Print status for specific package at a time")
    print("3.  Print status of all packages at a time")
    print("4.  Exit")

    print()
    options = int(input("Enter 1-4: "))
    if options == 1:
        for i in range(1, 41):
            print(my_hash.search(i))
            print()

    elif options == 2:
        #inputs
        package_number = int(input("Enter package number:  "))
        package_time = input("Enter time (HH:MM:SS):  ")

        #convert time to timedelta
        time_split = datetime.strptime(package_time, "%H:%M:%S")
        delta = timedelta(hours=time_split.hour, minutes=time_split.minute, seconds=time_split.second)

        #search for package
        search_package = (my_hash.search(package_number))

        #search for time
        print(search_package.status(delta))

    elif options == 3:
        #inputs
        package_time = input("Enter time (HH:MM:SS):  ")

        # convert time to timedelta
        time_split = datetime.strptime(package_time, "%H:%M:%S")
        delta = timedelta(hours=time_split.hour, minutes=time_split.minute, seconds=time_split.second)

        for i in range(1, 41):
            search_package = my_hash.search(i)
            print(search_package.status(delta))


    elif options == 4:
        break
