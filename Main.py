# # define a function to return the distance between two addresses of the function- distance_between_addresses(address1, address2)
from AddressData import address_list
from DistanceData import distance_list


def distance_between(index1, index2):
    address1 = address_list[index1]
    address2 = address_list[index2]
    distance = distance_list[index1][index2]

    return f"{address1} {address2} {distance}"


print(distance_between(6, 2))