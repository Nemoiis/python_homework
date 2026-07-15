import csv
import sys
import os
import custom_module
from datetime import datetime



# Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_number):
    idx = column_index("first_name")
    return employees["rows"][row_number][idx]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8
def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue  
        result[field] = row[i]
    return result

print(employee_dict(employees["rows"][0]))

# Task 9
def all_employees_dict(): 
    result = {}
    for row in employees["rows"]:
        key = row[employee_id_column]
        result[key] = employee_dict(row)
    return result

print(all_employees_dict())

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("nemo-was-here")
print(custom_module.secret)

# Task 12
def read_csv_as_dict_of_tuples(path):
    data = {}
    rows = []
    try:
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))
        data["rows"] = rows
        return data
    except Exception as e:
        print(f"An error occurred: {type(e).__name__} - {e}")
        sys.exit(1)

def read_minutes():
    minutes1 = read_csv_as_dict_of_tuples("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict_of_tuples("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)
# Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2  

minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes_as_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_as_list))
    return converted

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1]) 
    converted = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    try:
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted)
    except Exception as e:
        print(f"An error occurred: {type(e).__name__} - {e}")
        sys.exit(1)
    return converted

write_sorted_list()