x,y,z=(1,2,3)


options = ("rock", "paper", "scissors")

(rock, paper, scissors) = options

print("rock:", rock)
print("paper:", paper)
print("scissors:", scissors)            


#
# tuples are immutable, like strings, integers,floats, etc.  You cannot change the values of a tuple after it is created.  You can, however, create a new tuple that contains the values you want.
#

menu=('soup', 'salad', 'sandwich', 'pizza')


for item in menu:
    print(item, end=' ')

menu_copy=menu[:]
print("\nMenu copy:", menu_copy)
menu_copy=menu_copy+('ice cream',)
print("Menu copy after adding ice cream:", menu_copy)
print("Original menu:", menu)

count=(1,2,3,4,5,6,7,8,9,10)
copy=count[:]
print(id(copy)) # different id 

copy=copy+(1,)  # explain this  

print(id(copy)) # different id 

print(copy)