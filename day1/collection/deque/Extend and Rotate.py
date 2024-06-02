from collections import deque

# Creating a deque
dq = deque([1, 2, 3])

# Extend the right end
dq.extend([4, 5, 6])
print("Deque after extending to the right:", dq)

# Extend the left end
dq.extendleft([0, -1, -2])
print("Deque after extending to the left:", dq)

# Rotate the deque to the right by 2 steps
dq.rotate(2)
print("Deque after rotating to the right by 2 steps:", dq)

# Rotate the deque to the left by 3 steps
dq.rotate(-3)
print("Deque after rotating to the left by 3 steps:", dq)
