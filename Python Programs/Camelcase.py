
'''// python program to create function CamelCase(str)
take the str parameter being passsed 
and return it in proper camel case format 
where first letter of each work is captitalized. 
The string will only contain letters and 
some combination of delimiter unctuation charectors separating each word
write python code  Input is "cats AND*Dogs- are Awesome"'''

import re

# def CamelCase(str):
#     # split the string into words
#     result=""
#     words=re.split(r'[^a-zA-Z]',str)
#     # initialize the result string
#     for word in words:
#         result+=word.capitalize()
#     return result

# str1="cats dogs are awesome"
# str2="cats AND*Dogs- are Awesome"
# print(CamelCase(str2))


def camelCaseProgram(str):
    # split the string into words
    result=""
    words=re.split(r'[^a-zA-Z]',str)
    print(words)
    for word in words:
        result+=word.capitalize()+" "
        print(result)

    return result

str2="cats AND*Dogs- are Awesome"
print(camelCaseProgram(str2))  # Output: CatsDogsAreAwesome

