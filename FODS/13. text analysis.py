from collections import Counter

sample_text = """
This is a sample text. It contains some words , and some words are repeated. 
The goal is to calculate the frequency distribution of words in this text.
"""

text = sample_text.lower()

words = text.split()

freq = Counter(words)

print("Word Frequency Distribution:")
for word, frequency in freq.items():
    print(f"{word}: {frequency}")
