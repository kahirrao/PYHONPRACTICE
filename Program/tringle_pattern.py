print("-----------Inverted Right-Angled Number Triangle-----------")
n=6
for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(j, end="")
    print()


print("------Right-Angled Number Triangle----------------")

for i in range(1, n, +1):
    for j in range(1,i+1):
        print(j, end='')
    print()

print("----------------Floyds Triangle----------------")


for i in range(1, n, +1):
    num = 1
    for j in range(1,i+1):
        print(num,end="")
        num +=1
    print()


print("----------------Pascal Triangle----------------")

for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()