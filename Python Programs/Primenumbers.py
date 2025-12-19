#  Check number is prime or not
#  prime numbers are numbers that have only 2 factors: 1 and themselves. It can be divided by 1 or itself only.
def is_prime(n):
    if n<=1:
        print(n,"is not a prime number")
    else:
        count=0
        for i in range (1,n+1):
            if n%i==0:
                count=count+1
        if count==2:
            print(n,"is a prime number")
        else:
            print(n,"is not prime number")

n=int(input("Enter your number", ))
is_prime(n)


#######################################################################################################################

# Check if a number is prime or not
# Prime numbers are numbers that have only 2 factors: 1 and themselves. It can be divided by 1 or itself only.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter your number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
