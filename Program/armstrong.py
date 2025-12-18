
from numpy import power


num = 152
a=num
arm =0

while(num >0):
    rem = num % 10
    arm = arm + rem ** 3
    num = num // 10

if(a==arm):
    print(f"{a} is Armstrong")
else:
    print(f"{a} is Not Armstrong")