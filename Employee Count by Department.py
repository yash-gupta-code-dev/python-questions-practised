employees = [
    ("Alice", "HR"),
    ("Bob", "IT"),
    ("Charlie", "HR"),
    ("David", "IT"),
    ("Eva", "Finance"),
    ("John", "IT")
]


def count_employees(employees):
    employee_dict = {}
    for employee in employees:
        if employee[1] not in employee_dict:
            employee_dict[employee[1]] = {
                "employees" : [employee[0]],
                "count" : 1
            }
        else:
            employee_dict[employee[1]]["count"] += 1
            employee_dict[employee[1]]["employees"].append(employee[0])

    return employee_dict

employee_dict = count_employees(employees)
print(employee_dict)