a =[1,4,6,8,9]

max_val=a[0]
min_val=a[0]

for i in range(1,len(a)):
    if a[i] > max_val:
        max_val= a[i]
    if a[i] < min_val :
        min_val = [i]
        

print (f"{max_val} is Highest Number")
print (f"{min_val} is Lowest Number")