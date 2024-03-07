"""import faker"""
import json
import random
from faker import Faker
fake = Faker()
# Generating fake employee personal details
employee_records = []
for _ in range(random.randint(0,10)):
    employee_record = {
        "EMP ID": fake.uuid4(),
        "EMP NAME": fake.name(),
        "EMP EMAIL": fake.email(),
        "Business Unit": fake.company(),
        "Salary": fake.random_number(digits=5)
    }
    employee_records.append(employee_record)
# Writing employee personal details to JSON file
with open("employee_personal_details.json", "w",encoding="utf-8") as json_file:
    json.dump(employee_records, json_file, indent=4)
# Reading employee personal details from JSON file
with open("employee_personal_details.json", "r",encoding="utf-8") as json_file:
    employee_records = json.load(json_file)
# Aggregating employee details w.r.t Business Unit
employee_details_by_unit = {}
for record in employee_records:
    unit = record["Business Unit"]
    if unit not in employee_details_by_unit:
        employee_details_by_unit[unit] = []
    employee_details_by_unit[unit].append(record)
# Writing aggregated employee details to JSON file
with open("employee_details_by_unit.json", "w",encoding="utf-8") as json_file:
    json.dump(employee_details_by_unit, json_file, indent=4)
# Deleting employee details when contract is terminated
def terminate_employee(employee_id):
    """employee details"""
    for uni in employee_details_by_unit.values():
        for employe in unit:
            if employe["EMP ID"] == employee_id:
                uni.remove(employe)
                with open("terminated_employees.json", "a",encoding="utf-8") as terminated_file:
                    json.dump(employe["EMP NAME"], terminated_file)
                    terminated_file.write("\n")
                return
    raise ValueError("Employee not found")
salary_hike_percentages = {
    "Business Unit 1": 10,
    "Business Unit 2": 15,
    "Business Unit 3": 8
}
for unit, hike_percentage in salary_hike_percentages.items():
    for employee in employee_details_by_unit.get(unit, []):
        old_salary = employee["Salary"]
        new_salary = old_salary * (1 + hike_percentage / 100)
        employee["Salary"] = round(new_salary)
# Writing updated employee details to JSON file
with open("updated_employee_details.json", "w",encoding="utf-8") as json_file:
    json.dump(employee_details_by_unit, json_file, indent=4)
