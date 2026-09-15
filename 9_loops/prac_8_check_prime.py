#check prime number
 
def check_prime(num):
    if num<=1:
        return False
    for i in range(2,num//2):
        if num%i==0: return False

    return True

num=int(input("Enter a number: "))

print(f"{num} is prime number: {check_prime(num)}") 