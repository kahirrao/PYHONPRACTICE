#  Reverse words in a given string

str1="Welcome to python"

liststr=str1.split(" ")
print(liststr)
liststr.reverse()
liststr[-1::-1]
print(liststr)



def reverse_preserve_space(str):
    words=str.split(" ")
    result=""
    newstr=""
    for i in words:
        result=""
        for k in i:
            result=k+result
        
        result+=" "
        newstr+=result
    return newstr
         
        
print(reverse_preserve_space("Welcome to python"))  # Output: "emocleW ot nohtyp"


