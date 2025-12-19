#  Programs to print fibonacci series
# Fibonacci series is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

def fibonacci_series(n):
    n1=0
    n2=1
    count=0
    l1=[]
    if n<=0:
        print("Enter positive number")
    elif n==1:
        print("fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("fibonacci sequence:")
        while count<n+1:
            l1.append(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
        return l1
        
        

a=fibonacci_series(5)  
print(a)

b=fibonacci_series(10)
print(b)


