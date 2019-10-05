import csv
import re

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
VALID_COLUMN_HEADERS = ["name", "age", "number_of_known_languages"]

NAME_COLUMN = 0
AGE_COLUMN = 1
LANGUAGE_COLUMN = 2

def trim_whitespace(input_rows):
    for row in input_rows:
        for i in range(0, len(row)):
            row[i] = row[i].strip()


def validate_input_parameters(sort_flag, sort_order):
    assert sort_flag in VALID_SORT_FLAGS, "{} is not a valid sorting flag! Valid entries are {}".format(sort_flag, VALID_SORT_FLAGS)
    assert sort_order in VALID_SORT_ORDER, "{} is not a valid sorting order! Valid entries are {}".format(sort_order, VALID_SORT_ORDER)


def validate_row(row):
    assert re.search('[a-zA-Z] [a-zA-Z]', row[NAME_COLUMN]), "The name must include first and last names"
    assert re.search('\d', row[AGE_COLUMN]), "The age must only contain numbers"
    assert re.search('\d', row[LANGUAGE_COLUMN]), "The number of spoken lanuages must only contain numbers"


def sanitize_row(row):
    full_name = row[NAME_COLUMN]
    first_name, last_name = full_name.split()
    row[NAME_COLUMN] = first_name.capitalize() + " " + last_name.capitalize()


def validate_and_sanitize_csv_rows(input_rows):
    trim_whitespace(input_rows)

    header_row = input_rows[0]
    assert VALID_COLUMN_HEADERS == header_row, "{} are not valid column headers! The expected headers are {}".format(header_row, VALID_COLUMN_HEADERS)

    data_rows = input_rows[1:len(input_rows)]
    for row in data_rows:
        validate_row(row)
        sanitize_row(row)

    return input_rows


file_path, sort_flag, sort_order = input("Enter the file path, column to sort by, and the sorting order: ").split()

sort_flag = sort_flag.upper()
sort_order = sort_order.upper()

validate_input_parameters(sort_flag, sort_order)

with open(file_path, newline='') as input_file:
    input_rows = list(csv.reader(input_file))

validate_and_sanitize_csv_rows(input_rows)

