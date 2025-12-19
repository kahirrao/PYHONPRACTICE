#  How to identify max and min elements in array
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def max_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
        if arr[i] < min_element:
            min_element = arr[i]
    
    return max_element, min_element

# Example usage
max_element, min_element = max_min(arr2)
print("Maximum element:", max_element)
print("Minimum element:", min_element)
   

   
print(max_min(arr2))
        
# How to identify max and min elements in array suggest any other way than max() and min() functions

def maxmin(arr):
    max_ele=arr[0]
    min_ele=arr[0]
    for i in arr:
        if i>max_ele:
            max_ele=i
        elif i<min_ele:
            min_ele=i
    return max_ele,min_ele

arr=[1,2,3,4,5,6,7,8,9,10]
print(maxmin(arr))
