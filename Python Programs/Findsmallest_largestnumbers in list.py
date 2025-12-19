#  Smallest and largest number in the list

l1=[1,2,3,4,5,6,7,8,9,10]

def smallest_largest(l1):
    # l1.sort(reverse=True)
    smallest=largest=l1[0]
    for i in l1:
        if smallest>i:
            smallest=i
        elif largest<i:
            largest=i
    return smallest,largest

print(smallest_largest(l1))


