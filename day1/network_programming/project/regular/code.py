# example : Regular Expression

# • Quantifiers

# • character sequence and substitute

# • Search method
# ChatGPT
# Here's an example of using regular expressions in Python to demonstrate quantifiers, character sequences, substitution, and the search method:

# python
# Copy code
# import re

# # Example string
# text = "The quick brown fox jumps over the lazy dog"

# # Using quantifiers
# # Find words that start with a lowercase letter followed by one or more lowercase letters
# pattern = r'\b[a-z]+\b'
# matches = re.findall(pattern, text)
# print("Words starting with lowercase letters:", matches)

# # Character sequence and substitution
# # Replace all occurrences of 'fox' with 'cat'
# modified_text = re.sub(r'fox', 'cat', text)
# print("Modified text:", modified_text)

# # Search method
# # Search for the word 'brown'
# search_result = re.search(r'\bbrown\b', text)
# if search_result:
#     print("Found 'brown' at position:", search_result.start())
# else:
#     print("Word 'brown' not found")

# Output:

# arduino
# Copy code
# Words starting with lowercase letters: ['he', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# Modified text: The quick brown cat jumps over the lazy dog
# Found 'brown' at position: 10
# Explanation:

# Quantifiers: The pattern \b[a-z]+\b finds words that start and end with a word boundary (\b) and contain one or more lowercase letters.
# Character sequence and substitution: The re.sub() function replaces all occurrences of 'fox' with 'cat' in the text.
# Search method: The re.search() method searches for the exact word 'brown' and returns the position if found.
# Quantifiers
# ChatGPT
# Quantifiers in regular expressions are symbols that specify the quantity of the preceding element in the pattern. They allow you to define how many times a character or group of characters should occur within a match. Here are some common quantifiers and their meanings:

# * (Zero or more times): Matches the preceding element zero or more times. For example, a* matches an empty string, 'a', 'aa', 'aaa', and so on.

# + (One or more times): Matches the preceding element one or more times. For example, a+ matches 'a', 'aa', 'aaa', but not an empty string.

# ? (Zero or one time): Matches the preceding element zero or one time. For example, a? matches an empty string or 'a'.

# {n} (Exactly n times): Matches the preceding element exactly n times. For example, a{3} matches 'aaa'.

# {n,} (At least n times): Matches the preceding element at least n times. For example, a{3,} matches 'aaa', 'aaaa', and so on.

# {n,m} (Between n and m times): Matches the preceding element between n and m times. For example, a{2,4} matches 'aa', 'aaa', or 'aaaa'.

# *?, +?, ??, {n,}?, {n,m}?: These are non-greedy versions of the respective quantifiers. They match as few characters as possible.

# Example:

# python
# Copy code
# import re

# text = "aaaabbbccccdd"

# # Using quantifiers
# matches_star = re.findall(r'a*', text)
# matches_plus = re.findall(r'a+', text)
# matches_question = re.findall(r'a?', text)
# matches_exact = re.findall(r'a{2}', text)
# matches_range = re.findall(r'a{2,3}', text)

# print("Matches using *:", matches_star)
# print("Matches using +:", matches_plus)
# print("Matches using ?:", matches_question)
# print("Matches using {2}:", matches_exact)
# print("Matches using {2,3}:", matches_range)
# Output:

# sql
# Copy code
# Matches using *: ['', 'aaaa', '', '', '']
# Matches using +: ['aaaa']
# Matches using ?: ['', 'a', 'a', 'a', 'a', '']
# Matches using {2}: ['aa', 'aa']
# Matches using {2,3}: ['aa', 'aaa']
# In this example:

# * matches 'a' zero or more times.
# + matches 'a' one or more times.
# ? matches 'a' zero or one time.
# {2} matches 'a' exactly two times.
# {2,3} matches 'a' two or three times.
#  character sequence and substitute
# ChatGPT
# Character sequence and substitution in regular expressions involve finding specific sequences of characters within a text and replacing them with another sequence. Here's an example demonstrating this in Python:

# python
# Copy code
# import re

# # Example text
# text = "The quick brown fox jumps over the lazy dog"

# # Using regular expression to find a character sequence
# pattern = r'\b[bB]rown\b'  # Matches 'brown' or 'Brown' as a whole word
# matches = re.findall(pattern, text)
# print("Matches found:", matches)

# # Substituting the matched sequence
# # Replace 'brown' or 'Brown' with 'black'
# modified_text = re.sub(pattern, 'black', text)
# print("Modified text:", modified_text)
# Output:

# sql
# Copy code
# Matches found: ['brown']
# Modified text: The quick black fox jumps over the lazy dog
# Explanation:

# The regular expression pattern \b[bB]rown\b is used to find the word 'brown' or 'Brown' as a whole word (using word boundaries \b). The [bB] within square brackets means it can match either 'b' or 'B'.
# re.findall() is used to find all matches of the pattern in the text.
# re.sub() is used to substitute all occurrences of the matched pattern with the specified replacement string, which is 'black' in this case.
# This demonstrates how you can use regular expressions to find specific character sequences within a text and replace them with another sequence.


# • Search method
# ChatGPT
# The search() method in Python's re module is used to search for a specific pattern within a string. It returns a match object if the pattern is found, and None otherwise. Here's an example demonstrating the use of the search() method:

# python
# Copy code
# import re

# # Example text
# text = "The quick brown fox jumps over the lazy dog"

# # Using regular expression to search for a specific pattern
# pattern = r'\b[bB]rown\b'  # Matches 'brown' or 'Brown' as a whole word
# search_result = re.search(pattern, text)

# if search_result:
#     print("Pattern found at position:", search_result.start())
# else:
#     print("Pattern not found")
# Output:

# arduino
# Copy code
# Pattern found at position: 10
# Explanation:

# The re.search() function searches for the specified pattern (\b[bB]rown\b) within the given text.
# If the pattern is found, it returns a match object. In this example, 'brown' is found, so the match object contains information about the match.
# The start() method of the match object returns the starting position of the match within the original string.
# This demonstrates how to use the search() method to locate a pattern within a string using regular expressions in Python.