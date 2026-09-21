#sum of even number



size= int(input("Enter the size for sum of even numbers: "))
list=[]

for i in range(size):
    list.append(int(input("Enter the number: ")))




def sum_of_even(list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i
    return sum

print(sum_of_even(list)) #output: 30