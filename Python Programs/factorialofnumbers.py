#  How to find factorial of numbers

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1) 
    
# n=int(input("Enter your number", ))
# print("Factorial of",n,"is",factorial(n))


# Suggest any other method to find factorial of numbers

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter your number", ))
print("Factorial of",n,"is",factorial(n))