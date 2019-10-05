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

def trim_whitespace(rows):
    for row in rows:
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

def sort_rows(rows, sort_flag, sort_order):
    header_row = rows[0]
    data_rows = rows[1:len(rows)]

    if (sort_flag == 'N'):
        data_rows = sorted(data_rows, key = lambda row : row[NAME_COLUMN], reverse = bool(sort_order == 'D'))
    elif (sort_flag == 'A'):
        data_rows = sorted(data_rows, key = lambda row : row[AGE_COLUMN], reverse = bool(sort_order == 'D'))
    elif (sort_flag == 'L'):
        data_rows = sorted(data_rows, key = lambda row : row[LANGUAGE_COLUMN], reverse = bool(sort_order == 'D'))
    else:
        raise AssertionError("{} is not a valid sorting flag! Valid entries are {}".format(sort_flag, VALID_SORT_FLAGS))

    return [header_row] + data_rows


def pretty_print_rows(rows):
    header_row = rows[0]
    data_rows = rows[1:len(rows)]
    padding = 20

    formatted_header_row = "|".join(str(value).ljust(padding) for value in header_row)
    print(formatted_header_row)
    print("-" * len(formatted_header_row))
    for row in data_rows:
        print("|".join(str(value).ljust(padding) for value in row))


file_path, sort_flag, sort_order = input("Enter the file path, column to sort by, and the sorting order: ").split()

sort_flag = sort_flag.upper()
sort_order = sort_order.upper()

validate_input_parameters(sort_flag, sort_order)

with open(file_path, newline='') as input_file:
    input_rows = list(csv.reader(input_file))

rows = validate_and_sanitize_csv_rows(input_rows)
rows = sort_rows(rows, sort_flag, sort_order)
pretty_print_rows(rows)

