# A palindrome is a word that reads the same forward and backward. We can use a deque to efficiently check for palindromes.
from collections import deque

def is_palindrome(word):
    dq = deque(word)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Test the function
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
