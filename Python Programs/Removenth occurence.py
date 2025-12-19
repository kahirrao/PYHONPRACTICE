#  Remove nth occurence of the given word from the list
l1=["apple","banana","mango","apple","banana","mango","apple","banana","mango"]

# def remove_nth_occurence(l1,word,n):
#     count=0
#     for i in l1:
#         if i==word:
#             count+=1
#             if count==n:
#                 del l1[l1.index(i)]
#                 break
#     return l1
        
def remove_nth_occurence(l1,word,n):
    count=0
    for i in range (0,len(l1)-1):
        if l1[i]==word:
            count+=1
            if count==n:
                del l1[i]
                break
    return l1
print(remove_nth_occurence(l1,"apple",2))
        
