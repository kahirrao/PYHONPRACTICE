
count = 0
s = "Kalpesh Ahirrao"

for i in range(len(s)):
    if s[i] != ' ':
        count +=1
print(f"String Length Without Space: {count}")