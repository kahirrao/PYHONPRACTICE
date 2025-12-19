# check special charectors present in string.
import re

str1="Welcome to@@** python"

pattern=r"[!@#$%^&*()_+{}\[\]:;\"'<>?,./\\|`~]"
regex=re.compile(pattern)
if regex.search(str1)==None:
    print("No special charectors present in string")
else:  
    print("special charectors are present.")


# patt=r'[$@$]'
# reg=re.compile(patt)
# if reg.search(str1):
#     print("Special charectors are present.")
# else:
#     print("No special charectors present in string")

