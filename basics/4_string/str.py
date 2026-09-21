import copy

str = input("Enter your name: ")

sent="good evening"

greet="hello {} sir, nice to meet you {}"

print(greet.format(str,sent))

print("hello {} sir, nice to meet you {}".format(str,sent))

print(f"hello {str} sir, nice to meet you {sent}")

print(len(str))

deepCopy = str[:]
shallowCopy = str

print(deepCopy == str) # true ,because the values are same
print(deepCopy is str) # Usually True for strings, because Python may reuse/intern strings 

print(shallowCopy == str) # true ,because the values are same
print(shallowCopy is str) # Usually True for strings, because Python may reuse/intern strings , also shallowCopy is just another reference to the same string object as str



deepCopy = copy.deepcopy(str)
shallowCopy = copy.copy(str)

print(deepCopy == str) # true ,because the values are same
print(deepCopy is str) # false, because the memory address is different

print(shallowCopy == str) # true ,because the values are same
print(shallowCopy is str) # Usually True for strings, because Python may reuse/intern strings , also shallowCopy is just another reference to the same string object as str


menu=" 1. Coke, 2. Pepsi, 3. Sprite, 4. Fanta"

menuList=menu.split(",") # split the string into a list of items based on the comma delimiter
print(menuList) # [' 1. Coke', ' 2. Pepsi', ' 3. Sprite', ' 4. Fanta']


menu="coke,pepsi,sprite,fanta"

menuList=menu.split(",") # split the string into a list of items based on the comma delimiter
print(menuList) # ['coke', 'pepsi', 'sprite', 'fanta


str = "".join(menuList) # join the list of items into a single string without any separator
print(str) # 'cokepepsispritefanta'


str=" ".join(menuList) # join the list of items into a single string with a space separator
print(str) # 'coke pepsi sprite fanta'

print(",".join(menuList)) # join the list of items into a single string with ',' as separator   coke,pepsi,sprite,fanta'



data= """ 
    hello everyone, this is a multi-line string.
    It can span multiple lines and preserve the formatting.     
    and it can also include special characters like newlines (\n) and tabs (\t).
    also, it can be used to create docstrings for functions and classes.
"""


for word in data.splitlines(): # split the string into a list of lines based on newline character
    print(word) 


for word in data.split(): # split the string into a list of words based on whitespace
    print(word)



exampleString = "Hello \"Welcome to Python programming\" . " \
"This is a sample string that contains double quotes."

print(exampleString) # Hello "Welcome to Python programming" . This is a sample string that contains double quotes.


