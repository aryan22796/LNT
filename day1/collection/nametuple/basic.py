from collections import namedtuple

# Define a namedtuple type called 'Point' with fields 'x' and 'y'
name_tuple_access = namedtuple('variable_define', ['x', 'y','z'])
# Create an instance of Point
var = name_tuple_access(10, 20,30)

# Access fields using dot notation
print(var.x)  # Output: 10
print(var.y)  # Output: 20
