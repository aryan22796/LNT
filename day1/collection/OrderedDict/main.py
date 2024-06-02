from collections import OrderedDict

def count_words_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        ordered_counter = OrderedDict()
        for word in words:
            if word in ordered_counter:
                ordered_counter[word] += 1
            else:
                ordered_counter[word] = 1
        return ordered_counter

# Counting words in each file
ordered_counter1 = count_words_in_file('file1.txt')
ordered_counter2 = count_words_in_file('file2.txt')

# Combining counts from both files while maintaining order
total_counter = OrderedDict()
for counter in (ordered_counter1, ordered_counter2):
    for key, value in counter.items():
        if key in total_counter:
            total_counter[key] += value
        else:
            total_counter[key] = value

print(f"File1 counts: {ordered_counter1}")
print(f"File2 counts: {ordered_counter2}")
print(f"Total counts: {total_counter}")
