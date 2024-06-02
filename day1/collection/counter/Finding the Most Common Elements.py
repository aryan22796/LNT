from collections import Counter

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(data)
most_common = counter.most_common(2)
print(most_common)
# Combining Counters and Arithmetic Operations

counter1 = Counter(a=4, b=2, c=0, d=-2)
counter2 = Counter(a=1, b=2, c=3, d=4)
combined_counter = counter1 + counter2  # Combine counts
print(combined_counter)
