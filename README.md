# python-csv-parser
This is a project to ingest a CSV file and gain some observations from the data. This file contains a name (first & last), age, and number of spoken languages. Create a program that will ingest this CSV, clean & validate the input, and allow us to sort the data.

The input will be 3 values:
1. String file_path (e.g. `~/Programs/Input/input.csv`)
2. Character sort_flag (`n` for name, `a` for age, or `l` for number of spoken languages, case-insensitive)
3. Character sort_order (`a` for ascending or `d` for descending, case-insensitive)

### Notes:
* The CSV will start with a header that contains the column names, all future rows will be data points
    * `name`, `age`, `number_of_known_languages`
* The data will need to be sanitized, handle the following cases:
    * Leading/trailing whitespace
    * Poorly capitalized names (e.g. `joHN DOe`)
* If the file has invalid data, we should alert the user, handle the following cases:
    * "Name" must include the first and last name
    * Columns must be in order (avoid non-alphabetical values in the name column or non-numeric values in the number columns
