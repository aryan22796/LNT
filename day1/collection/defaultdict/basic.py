from collections import defaultdict

# Create a defaultdict with a default value of 0 for non-existent keys
d = defaultdict(int)

# Add some values
d['a'] = 1
d['b'] = 2

# Access a non-existent key
print(d['c'])  # Output: 0

# Counting Elements
# This example demonstrates how defaultdict can be used to count the number of occurrences of each character in a string.

from collections import defaultdict

# Create a defaultdict with a default value of 0 for non-existent keys
char_count = defaultdict(int)

# String to count characters
s = "hello world"

# Count each character
for char in s:
    char_count[char] += 1

print(char_count)


#  Grouping Items
# This example shows how to group items in a list based on their lengths.
from collections import defaultdict

# List of words
words = ["apple", "bat", "bar", "atom", "book", "cat"]

# Create a defaultdict with a default value of an empty list for non-existent keys
grouped_words = defaultdict(list)

# Group words by their length
for word in words:
    grouped_words[len(word)].append(word)

print(grouped_words)


# Example 3: Nested Dictionary
# Using defaultdict, you can easily create nested dictionaries without initializing each level.

from collections import defaultdict

# Create a defaultdict of defaultdicts
nested_dict = defaultdict(lambda: defaultdict(int))

# Add values
nested_dict['A']['a'] = 1
nested_dict['A']['b'] = 2
nested_dict['B']['a'] = 3

print(nested_dict)


# Example 4: Default Factory with Custom Function
# You can use a custom function as the default factory.

from collections import defaultdict

# Custom default factory
def default_value():
    return "default"

# Create a defaultdict with a custom default factory
d = defaultdict(default_value)

# Access a non-existent key
print(d['key'])  # Output: default


# Example 5: Using defaultdict for a Graph
# defaultdict can be used to represent a graph where each node's edges are stored in a list.


from collections import defaultdict

# Create a defaultdict of lists to represent a graph
graph = defaultdict(list)

# Add edges to the graph
graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('D')

print(graph,"done")


