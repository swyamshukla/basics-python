import random

print(random.random()) 

choice=['apple','banana','orange','grape']

ref=iter(choice)

for r in ref:
    if not r: break
    print(r) #output:apple


ref=iter(choice)

while True:
    if not ref.__next__(): break
    print(ref.__next__()) #output


dct = {"name":"John","age":30,"city":"New York"}

i = iter(dct)

for next in i:
    print(next.__next__()) #output:

