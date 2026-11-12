employee = {
    "name": "Alex",
    "salary": 3000,
    "role": "Data Engineer"
}

print(employee["name"])  # Output: Alex
print(employee["role"])  # Output: Data Engineer

employee["salary"] = 4000  # Update salary

employee["location"] = "London"  # Add new key-value pair

print(employee)  # Output: {'name': 'Alex', 'salary': 4000, 'role': 'Data Engineer', 'location': 'London'}
print(len(employee))  # Output: 4


salary = 3000

if(salary > 3500):
    print("Above threshold")  # Output: Above threshold
else:
    print("Below or equal to threshold")  # Output: Below or equal to threshold

salary = 4000

if(salary > 3500):
    print("Above threshold")  # Output: Above threshold
else:
    print("Below or equal to threshold")  # Output: Below or equal to threshold


employees = [
    {"name": "Alex", "salary": 3000},
    {"name": "Sarah", "salary": 4500},
    {"name": "John", "salary": 3500}
]

print(employees[0]["name"])  # Output: Alex
print(employees[1]["salary"])  # Output: 4500

employees[2]["salary"] = 4000  # Update salary for John
employees[0]["department"] = "IT"  # Add department for Alex

print(employees)  # Output: [{'name': 'Alex', 'salary': 3000, 'department': 'IT'}, {'name': 'Sarah', 'salary': 4500}, {'name': 'John', 'salary': 4000}]

if (employees[1]["salary"] > 4000):
    print("Salary exceeds 4000")  # Output: Sarah has a salary above 4000
else:
    print("Salary does not exceed 4000")  # Output: Salary does not exceed 4000

for employee in employees:
    print(employee["name"])  # Output: Alex, Sarah, John
    print(employee["salary"])  # Output: 3000, 4500, 4000
    if employee["salary"] > 3500:
        print("High salary")  # Output: High salary for Sarah and John
    else:
        print("Standard salary")  # Output: Standard salary for Alex