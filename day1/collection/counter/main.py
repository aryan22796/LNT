from collections import Counter

def count_words_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        return Counter(words)

# Counting words in each file
counter1 = count_words_in_file('file1.txt')
counter2 = count_words_in_file('file2.txt')

# Combining counts from both files
total_counter = counter1 + counter2

print(f"File1 counts: {counter1}")
print(f"File2 counts: {counter2}")
print(f"Total counts: {total_counter}")
