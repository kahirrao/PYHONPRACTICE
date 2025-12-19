a = [3, 56, 12, 89, 23, 4, 6]
n = len(a)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if a[j] > a[min_index]:
            min_index = j

    # swap after finding minimum
    a[i], a[min_index] = a[min_index], a[i]

b = list(a)
print(b)
