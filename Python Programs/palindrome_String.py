#  Palindrome string program

str=input("Enter your string: ")

# def palindrom_string(str):
#     if str==str[::-1]:
#         return "String is palindrome"
#     else:
#         return "String is not palindrome"
    
# print(palindrom_string(str))


# dnd 
def palindrome_other(str):
    str1=""
    for i in str:
        str1=i+str1
        print(str1)
    if str==str1:
        return "String is palindrome"
    else:
        return "String is not palindrome"
    
print(palindrome_other(str))


# python program to check if number is palindrome or not

# num=int(input("Enter your number: "))

# def palindrome_number(num):
#     temp=num
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     if temp==rev:
#         return "Number is palindrome"
#     else:
#         return "Number is not palindrome"

