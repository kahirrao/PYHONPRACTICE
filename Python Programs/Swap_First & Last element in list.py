# swap first and last element in list

def swap_first_last_element(l1):
    if len(l1)<2:
        return l1
    else:
        temp=l1[0]
        l1[0]=l1[-1]
        l1[-1]=temp
        return l1
l1=[1,2,3,4,5,6,7,8,9,10]
print(swap_first_last_element(l1))


