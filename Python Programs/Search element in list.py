#  Search an element in list

l1=["school","college","university","office","home","temple","church","mosque","gurudwara","hospital"]

def search_element(l1,ele):
    if ele in l1:
        return "Element found"
    else:
        return "Element not found"
    
print(search_element(l1,"office"))

##########################################################################################
ele=input("Enter the element to search:")
flag=0
for i in l1:
    if i==ele:
        flag+=1
        break

if flag==1:
    print("Element found")
else:
    print("Element not found")  

