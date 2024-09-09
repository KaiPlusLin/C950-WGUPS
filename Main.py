# # define a function to return the distance between two addresses of the function- distance_between_addresses(address1, address2)
from DistanceData import distance_list


def distance_between_addresses(address1, address2):
    distance = distance_list[address1][address2]
    print(distance)


distance_between_addresses(6, 2)