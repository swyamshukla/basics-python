# Multiplication Table Printer 
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
# Example: If the input number is 3, the output should be:
# 3 x 1=3
# 3 x 2=6
# 3 x 3=9
# 3 x 4=12
# 3 x 6=18
# 3 x 7=21
# 3 x 8=24
# 3 x 9=27
# 3 x 10=30

num=int(input("Enter the number: ")) #input: 3

def table(num):
    for i in range(1,11):
        if i !=5:
            print(f"{num} * {i} = {num*i}")

table(num) #output: 3 * 1 = 3
