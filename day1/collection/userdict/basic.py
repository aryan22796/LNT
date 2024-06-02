from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)

d = MyDict()
d['a'] = 1  # Output: Setting a to 1
print(d)  # Output: {'a': 1}
# Example 2: Default Value for Missing Keys
# This example demonstrates a dictionary that returns a default value for missing keys:

# python
# Copy code
from collections import UserDict

class DefaultDict(UserDict):
    def __init__(self, default=None):
        super().__init__()
        self.default = default

    def __getitem__(self, key):
        return self.data.get(key, self.default)

d = DefaultDict(default=0)
print(d['a'])  # Output: 0
d['b'] = 2
print(d['b'])  # Output: 2
# Example 3: Case-Insensitive Dictionary
# This example shows a dictionary that treats keys as case-insensitive:

# python
# Copy code
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __delitem__(self, key):
        super().__delitem__(key.lower())

d = CaseInsensitiveDict()
d['Key'] = 'value'
print(d['key'])  # Output: value
# Example 4: Logging Dictionary Access
# This example logs access to the dictionary:

# python
# Copy code
from collections import UserDict

class LoggingDict(UserDict):
    def __getitem__(self, key):
        value = super().__getitem__(key)
        print(f"Accessed {key}: {value}")
        return value

    def __setitem__(self, key, value):
        print(f"Set {key} to {value}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        print(f"Deleted {key}")
        super().__delitem__(key)

d = LoggingDict()
d['a'] = 1  # Output: Set a to 1
d['b'] = 2  # Output: Set b to 2
print(d['a'])  # Output: Accessed a: 1
del d['b']  # Output: Deleted b
# These examples illustrate how UserDict can be used to extend and customize the behavior of dictionaries in Python.


# UserString example 
# ChatGPT
# The UserString class in Python is part of the collections module, designed to create wrapper objects around string-like data. This class allows you to create custom string-like objects with additional functionality or behavior.

# Here's an example demonstrating the usage of UserString:

# python
# Copy code
from collections import UserString

class MyString(UserString):
    def double(self):
        """
        Returns the string concatenated with itself.
        """
        return self.data + self.data

    def reverse(self):
        """
        Returns the reversed string.
        """
        return self.data[::-1]

# Creating an instance of MyString
my_str = MyString("Hello, world!")

# Using custom methods
print("Original:", my_str)  # Output: Original: Hello, world!
print("Doubled:", my_str.double())  # Output: Doubled: Hello, world!Hello, world!
print("Reversed:", my_str.reverse())  # Output: Reversed: !dlrow ,olleH



