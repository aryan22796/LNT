# Iterating in Order
from collections import OrderedDict

# Basic example: maintaining insertion order
ordered_dict = OrderedDict([('banana', 3), ('apple', 4), ('pear', 1)])
for key, value in ordered_dict.items():
    print(f'{key}: {value}')