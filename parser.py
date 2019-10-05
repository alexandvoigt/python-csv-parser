import csv

file_path, sort_flag, sort_order = input("Enter the file path, column to sort by, and the sorting order: ").split()

with open(file_path, newline='') as input_file:
    rows = list(csv.reader(input_file))

