# How to find length of list

l1=[1,2,3,4,5,6,7,8,9,10]

def lengthoflist(l1):
    count=0
    for i in l1:
        count=count+1
    return count

print(lengthoflist(l1))