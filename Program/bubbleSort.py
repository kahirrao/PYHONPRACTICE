a = [3, 4, 6, 23, 8, 2]
n = len(a)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

b = list(a)
print(b)
