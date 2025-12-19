
l1 = [3, 6 , 1 ,8 ,34, 78]

l2=[]
for i in range (len(l1)-1,-1,-1):
    l2.append(l1[i])

print(l2)

print("---------------------")
l2 = l1[::-1]
print(l2)
print("---------------------")
l1.reverse()
print(l1)