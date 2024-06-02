from collections import Counter

sentence = "the quick brown fox jumps over the lazy dog the fox was quick"
words = sentence.split()
word_counter = Counter(words)
print(word_counter)
