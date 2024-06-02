# from collections import Counter

# # Create a Counter
# cnt = Counter(['a', 'b', 'c', 'a', 'b', 'b'])

# print(cnt)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})

# # Access count of an element
# print(cnt['a'])  # Output: 2

# # Get the most common elements
# print(cnt.most_common(2))  # Output: [('b', 3), ('a', 2)]
from collections import Counter

# Basic example: counting characters in a string
s = "hello world"
counter = Counter(s)
print(counter)
