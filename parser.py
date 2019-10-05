import csv

valid_sort_flags = {'N', 'A', 'L'}
valid_sort_order = {'A', 'D'}



def validate_input_parameters(sort_flag, sort_order):
    if sort_flag not in valid_sort_flags:
        print ("{} is not a valid sorting flag! Valid entries are {}".format(sort_flag, valid_sort_flags))
    if sort_order not in valid_sort_order:
        print ("{} is not a valid sorting order! Valid entries are {}".format(sort_order, valid_sort_order))



file_path, sort_flag, sort_order = input("Enter the file path, column to sort by, and the sorting order: ").split()

sort_flag = sort_flag.upper()
sort_order = sort_order.upper()

validate_input_parameters(sort_flag, sort_order)

with open(file_path, newline='') as input_file:
    rows = list(csv.reader(input_file))

