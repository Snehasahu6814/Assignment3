"""import faker TO create the random data"""
import json
import random
from faker import Faker
# Initialize Faker to generate fake data
fake = Faker()
# Generate fake employee personal details
employee_details = []
for _ in range(random.randint(10, 20)):
    emp_id = fake.uuid4()
    emp_name = fake.name()
    emp_email = fake.email()
    business_unit = fake.company()
    salary = fake.random_number(digits=5)
    employee_details.append({
        "EMP ID": emp_id,
        "EMP NAME": emp_name,
        "EMP EMAIL": emp_email,
        "Business Unit": business_unit,
        "Salary": salary
    })
# Write data to JSON file
with open("Employee_Personal_Details.json", "w",encoding="utf-8") as json_file:
    json.dump(employee_details, json_file, indent=4)
print("Employee personal details generated and saved in 'Employee_Personal_Details.json'")
