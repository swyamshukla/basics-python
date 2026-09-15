#find the first non repeatitive character in a string

str = input("Enter a string: ")


#hello

def first_non_repeating_char(str):
    for i in range(0,len(str)):
        for j in range(0,len(str)):
             if i!= j and str[i]==str[j]:
                continue
        return str[i]


print("First non-repeating character is:", first_non_repeating_char(str)) #output
    