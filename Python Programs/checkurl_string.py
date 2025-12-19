#  check url in string
import re

str1="Welcome to python. Visit my website https://www.python.org"

pattern=r"https://[a-zA-Z0-9]* +\.[a-zA-Z][2-3]"
regex=re.compile(pattern)
if regex.findall(str1)==None:
    print("No url present in string")
else:
    print("Url present in string")
    