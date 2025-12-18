
s = "Kalpesh"
rev = " "

b = ''.join(reversed(s))
c = s[::-1]
# for ch in s:
#     rev = ch + rev  
# for i in range(len(s)-1, -1, -1):
#     rev = rev + s[i]
for i in range(len(s)):
    rev = s[i] + rev
print(rev)
print(b)
print(c)
