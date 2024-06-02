from collections import deque
# Example 1: Basic Append and Pop Operations
# Creating a deque
dq = deque()

# Append elements to the right
dq.append(1)
dq.append(2)
dq.append(3)

# Append elements to the left
dq.appendleft(0)

print("Deque after appending:", dq)

# Pop elements from the right
print("Popped from right:", dq.pop())

# Pop elements from the left
print("Popped from left:", dq.popleft())

print("Deque after popping:", dq)

