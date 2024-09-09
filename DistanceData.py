import csv

def load_data(filename):
    my_list = []
    with open(filename) as distances:
        distance_data = csv.reader(distances, delimiter=',')
        for row in distance_data:
            my_list.append(row)
    return my_list

distance_list = load_data('CSV files/distanceCSV.csv')
# for row in distance_list:
#     print(row)
#return float(distance_list[9][4])
