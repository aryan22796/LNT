from collections import ChainMap

# Two basic dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Creating a ChainMap
chain = ChainMap(dict1, dict2)

# Accessing values
print(chain['a'])  # Output: 1 (from dict1)
print(chain['b'])  # Output: 2 (from dict1, because dict1 is searched first)
print(chain['c'])  # Output: 4 (from dict2)

# Modifying values
chain['a'] = 10
print(dict1['a'])  # Output: 10
