#  Python program to swap any elements in list
l1=[1,2,3,4,5,6,7,8,9,10]
def swap_any_element(l1,a,b):
    if len(l1)<2:
        return l1
    else:
        if a<len(l1) and b<len(l1):
            l1[a],l1[b]=l1[b],l1[a]
        else:
            return "Index out of range"
    return l1
    

print(swap_any_element(l1,1,5)) 
    
