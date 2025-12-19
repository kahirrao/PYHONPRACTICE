#  Count of occurence of element in list

l1=["apple","banana","mango","apple","banana","mango","apple","banana","mango"]

def count_occurence(l1,word):
    count=0
    for i in l1:
        if i==word:
            count+=1
    return count

print(count_occurence(l1,"apple"))

#  Count of occurence of all elements in list

l2=["apple","banana","mango","apple","banana","mango","apple","banana","mango"]

def count_occurence_all(l2):
    dict1={}
    for i in l2:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1

    return dict1

print(count_occurence_all(l2))

