# Python program to identify that charector is vowel or consonant

def charector(ch):
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        return "Vowel"
    else:
        return "Consonant"
    
print(charector('a'))