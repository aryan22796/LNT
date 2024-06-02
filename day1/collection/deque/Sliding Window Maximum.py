# Given an array and a sliding window size k, find the maximum value in each window.
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    max_values = []

    for i, num in enumerate(nums):
        # Remove elements not within the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements in k range as they are useless
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Append the maximum value of the current window
        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values

# Test the function
print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]


