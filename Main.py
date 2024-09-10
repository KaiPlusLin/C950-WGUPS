import csv
from datetime import timedelta
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


#print(distance_between(6, 2))

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


def deliver_packages(truck):

    while len(truck.current_packages) > 0:
        min_distance = 2000  # miles
        closest_package = None

        for package_id in truck.current_packages:
            package = my_hash.search(package_id)
            truck_location = truck.current_location
            package_address = package.address
            distance = distance_between(truck_location, package_address)

            if distance < min_distance:
                min_distance = distance
                closest_package = package

        truck.mileage += min_distance
        truck.current_time += timedelta(hours=min_distance / 18)
        closest_package.delivery_time = truck.current_time
        closest_package.delivery_status = "DELIVERED"
        truck.location = closest_package.address
        truck.current_packages.remove(closest_package)

        # my_hash.insert(closest_package.id, closest_package)


    return truck.mileage


truck1 = Truck(1, [4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 19, 20, 29, 30, 31] ,timedelta(hours=8))
truck2 = Truck(2, [1, 3, 18, 34, 36, 37, 38, 40], timedelta(hours=8))
truck3 = Truck(3, [2, 6, 9, 17, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39], timedelta(hours=8))

#
# for package in truck1.current_packages:
#     print(package)
# for package in truck2.current_packages:
#     print(package)
# for package in truck3.current_packages:
#     print(package)

# Console

