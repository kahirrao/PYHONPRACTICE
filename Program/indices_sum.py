
a = [1,3,5,13,6,9]
sum = 8

for i in range (len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == sum:
            print(f" Indicies : {i} , {j}")