# Let's say we are working on a program that processes a list of employee records, 
# and each record includes the employee's name, age, and job title.
#  Using a namedtuple can make the code cleaner and more readable.
from collections import namedtuple

# Define a namedtuple type called 'Employee' with fields 'name', 'age', and 'job'
Employee = namedtuple('Employee', ['name', 'age', 'job'])

# Create instances of Employee
employee1 = Employee(name='Alice', age=30, job='Engineer')
employee2 = Employee(name='Bob', age=35, job='Manager')

# Access fields using dot notation
print(employee1.name)  # Output: Alice
print(employee2.age)   # Output: 35
print(employee1.job)   # Output: Engineer

# Iterate over a list of employees
employees = [employee1, employee2]
for emp in employees:
    print(f"{emp.name} is a {emp.age}-year-old {emp.job}.")



# Advantages of namedtuple
# Readability: Named fields make the code more self-explanatory and easier to understand.
# Immutability: Helps ensure that the data is not modified accidentally, promoting safer code.
# Efficiency: Namedtuples are more memory-efficient compared to dictionaries or custom classes
# because they do not require per-instance __dict__ overhead.