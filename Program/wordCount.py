
print("--------------- Using COunt()----------------")
text = "python is easy and python is powerful"
words = text.split()

for word in set(words):
    print(word, ":", words.count(word))

print("--------------- Collection Counter----------------")
from collections import Counter

text = "python is easy and python is powerful"
words = text.split()

freq = Counter(words)

for word, count in freq.items():
    print(word, ":", count)

print("--------------- Case-insensitive word occurrence----------------")
text = "Python is easy and python is Powerful"

words = text.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
