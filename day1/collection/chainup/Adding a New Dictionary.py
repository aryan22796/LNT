from collections import ChainMap

dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}

# Creating a ChainMap
chain = ChainMap(dict1, dict2)

# Adding a new dictionary
dict3 = {'w': 5, 'x': 6}
chain = chain.new_child(dict3)

print(chain['w'])  # Output: 5
print(chain['x'])  # Output: 6 (from dict3)
print(chain['y'])  # Output: 2 (from dict1)
