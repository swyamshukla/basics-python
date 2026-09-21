import random



def calc():
    len =int(input("Enter the length of the list:" ))
    wid = int(input("Enter the width of the list:"))
    result = ((len+wid)*2,len*wid)
    return result


(circum,area)= calc()

print(f"circumference: {circum}")
print(f"area: {area} ")

