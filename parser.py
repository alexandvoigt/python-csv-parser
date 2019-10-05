import csv

'''
Sort Flags:
- N = Name
- A = Age
- L = Number of known languages

Sort Order:
- A = Ascending
- D = Descending
'''
VALID_SORT_FLAGS = {'N', 'A', 'L'}
VALID_SORT_ORDER = {'A', 'D'}



def validate_input_parameters(sort_flag, sort_order):
    if sort_flag not in VALID_SORT_FLAGS:
        print ("{} is not a valid sorting flag! Valid entries are {}".format(sort_flag, VALID_SORT_FLAGS))
    if sort_order not in VALID_SORT_ORDER:
        print ("{} is not a valid sorting order! Valid entries are {}".format(sort_order, VALID_SORT_ORDER))



file_path, sort_flag, sort_order = input("Enter the file path, column to sort by, and the sorting order: ").split()

sort_flag = sort_flag.upper()
sort_order = sort_order.upper()

validate_input_parameters(sort_flag, sort_order)

with open(file_path, newline='') as input_file:
    rows = list(csv.reader(input_file))

