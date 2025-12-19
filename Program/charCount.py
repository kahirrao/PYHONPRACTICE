print("----------------------------------")
from collections import Counter

text = "python programming"
char_count = Counter(text)

print(char_count)

print("-----------Without Counting Space-----------------------")
text = "python programming"
char_count = {}

for ch in text:
    if ch != " ":
        char_count[ch] = char_count.get(ch, 0) + 1

print(char_count)

print("-----------With Counting Space-----------------------")
text = "python programming"

char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

for ch, count in char_count.items():
    print(ch, ":", count)

