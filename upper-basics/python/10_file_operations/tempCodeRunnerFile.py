
dct = {"name":"John","age":30,"city":"New York"}

i = iter(dct)

for next in i:
    print(next.__next__()) #output:

