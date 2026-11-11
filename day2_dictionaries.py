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

