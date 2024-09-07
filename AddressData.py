import csv

def load_data(filename):
    my_list = []
    with open(filename) as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        next(address_data)
        for row in address_data:
            my_list.append(row)
    return my_list

address_list = load_data('CSV files/addressCSV.csv')
for row in address_list:
    print(row)
