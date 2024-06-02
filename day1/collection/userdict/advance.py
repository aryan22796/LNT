# In this example:

# We define a custom class MyString that inherits from UserString.
# We add two custom methods, double() and reverse(), to provide additional functionality to the string.
# We create an instance of MyString with the string "Hello, world!".
# We demonstrate the usage of the custom methods double() and reverse() on the instance.
# UserString provides a convenient way to create string-like objects with custom behavior, allowing you to extend the functionality of strings in Python.

# theory 
# ChatGPT
# The UserString class in Python's collections module is a wrapper class that acts as a proxy for string objects, providing a way to create string-like objects with extended or modified behavior. Here's a theoretical overview:

# Inheritance and Composition
# Inheritance: UserString is a subclass of MutableSequence, a built-in class for sequences that can be modified. This means it inherits all the behaviors and methods of MutableSequence, including methods like __getitem__, __setitem__, __delitem__, __len__, etc.

# Composition: UserString wraps around a string object (usually an instance of str). The actual string data is stored within the data attribute of the UserString instance.

# Immutability and Mutability
# Immutability: Instances of UserString are immutable by default. This means that once created, the contents of the string cannot be changed. This behavior is consistent with Python's built-in string objects (str), providing familiarity and consistency.

# Mutability: Although instances of UserString are immutable, you can subclass UserString to create mutable string-like objects by overriding appropriate methods such as __setitem__ and __delitem__.

# Customization
# Method Overriding: You can override methods inherited from MutableSequence to customize the behavior of the UserString object. For example, you can override __getitem__ to implement slicing differently or __add__ to customize string concatenation.

# Additional Functionality: You can add custom methods to provide additional functionality specific to your use case. For instance, you could add methods for string manipulation, formatting, or validation.

# Use Cases
# Custom String Operations: When you need string-like objects with specialized behavior not provided by Python's built-in string methods.

# Enhanced String Handling: When you need to handle strings in a more sophisticated or domain-specific way, such as parsing, validation, or transformation.

# Interfacing with External Systems: When you need to adapt string data to conform to specific interfaces or protocols used by external systems or APIs.

# Example Use Case
# Imagine you're building a text processing application where you need to represent strings with additional metadata, such as the source of the string or its formatting. You could use a UserString subclass to create string-like objects that include this metadata and provide methods for accessing or manipulating it.

# python

from collections import UserString

class MetadataString(UserString):
    def __init__(self, data, source=None):
        super().__init__(data)
        self.source = source

    def get_source(self):
        return self.source

# Usage
text = MetadataString("Hello, world!", source="user_input")
print(text)  # Output: Hello, world!
print(text.get_source())  # Output: user_input
# In this example, MetadataString is a subclass of UserString that includes additional metadata about the source of the string. This allows you to associate extra information with string objects while retaining all the functionalities of regular strings.


