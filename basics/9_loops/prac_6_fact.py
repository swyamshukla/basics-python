#factorial using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)*n

#using for-loop 

def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

#using while-loop

def fact_while():
    n=int(input("Enter a number: "))
    factorial=1
    i=1
    while i<=n:
        factorial*=i
        i+=1
    print(factorial) #output:120
        
