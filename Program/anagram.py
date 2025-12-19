str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")

print("-------------------------------------------")

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

print(is_anagram("listen", "silent"))
