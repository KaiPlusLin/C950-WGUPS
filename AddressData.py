import csv

def load_data(filename):
    my_list = []
    with open(filename) as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        for row in address_data:
            my_list.append(row)
    return my_list

def get_address_index(address):
    for index, addr in enumerate(address_list):
        if addr[2] == address:
            return index
    return None

address_list = load_data('CSV files/addressCSV.csv')
