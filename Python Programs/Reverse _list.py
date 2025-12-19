

# # Python program to reverse a list
l1=[1,2,3,4,5,6,7,8,9,10]

# # l1.reverse()
# # print(l1)

# print(l1[::-3])
# # Using slicing
# print(l1[::-1])

# # using for loop reversing list

l2=[]
for i in range (len(l1),-1,-1):
    l2.append(i)

print(l2)