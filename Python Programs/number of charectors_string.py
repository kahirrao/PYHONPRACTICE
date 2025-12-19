#  Count the number of charectors in string.

def count_charectors(s):
    count=0
    for ch in s:
        count+=1
    return count

s="Welcomee"
print(count_charectors(s))