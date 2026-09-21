#wap for count positive number in list

list=[1,2,3,-4,-5]

def count_positive(list):
    count=0
    for i in list:
        if i>0  :
            count+=1
    return count

print(count_positive(list)) #output:3
