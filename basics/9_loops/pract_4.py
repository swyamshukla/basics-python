#Reverse a String


str = input("Enter a string: ")

#"SWYAM"
#reverse: "MAYWS"


#Method 1: Using slicing
def reverse(str):
    return str[::-1]

#Method 2: Using for loop

def reverse_loop(str):
    reverse_str=""
    for ch in str:
        reverse_str=ch+reverse_str
    return reverse_str

print(reverse_loop(str))

print(reverse(str))
