
l = [10,34,2,5,19]
largest = 0
secLargest = 0

for i in range(len(l)):
    if l[i] > largest:
        secLargest = largest
        largest = l[i]
    elif l[i] > secLargest & l[i] != largest:
        secLargest = l[i]
print(secLargest)
