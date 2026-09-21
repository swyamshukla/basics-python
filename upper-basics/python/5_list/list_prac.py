# menu=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# print(menu[0:5]) # prints first 5 items
# print(menu[5:8]) # prints items from index 5 to index 8 (not including index 8)
# print(menu[:3]) # prints items from start to index 3 (not including index 3)
# print(menu[2:7]) # prints items from index 2 to index 7 (not including index 7)
# print(menu[-3:]) # prints last 3 items


# count=[0,1,2,3,4,5,6,7,8,9]
# print(count[::2]) # prints every second item [0, 2, 4, 6, 8]
# print(count[1:8:2]) # prints items from index 1 to index 8 (not including index 8) with a step of 2 [1, 3, 5, 7]
# print(count[::-1]) # prints the list in reverse order [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(count[3:0:-1]) # prints items from index 3 to index 0 (not including index 0) in reverse order [3, 2, 1]
# print(count[5:2:-1]) # prints items from index 5 to index 2 (not including index 2) in reverse order [5, 4, 3]

# print(menu)
# menu[1:1] = ["samosa", "chowmein"] # inserts "samosa" and "chowmein" at index 1
# print(menu) # prints the updated menu list
# menu[2:5] = ["momos", "pasta"] # replaces items from index 2 to index 5 (not including index 5) with "momos" and "pasta" 

# menu[3:4] = [] # removes the item at index 3

# print(menu) # prints the updated menu list after removal

# menu[1:1]=[] # what is diff between this and the above line? This line does not remove any items, it just inserts an empty list at index 1, which has no effect on the list. The above line removes the item at index 3.

# print(menu) # prints the updated menu list after inserting an empty list at index 1

# menu[1:3] = ["burger", "pizza"] # replaces items from index 1 to index 3 (not including index 3) with "burger" and "pizza"
# print(menu) # prints the updated menu list after replacement ['apple', 'burger', 'pizza', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']


count=[0,1,2,3,4,5,6,7,8,9]

for i in count:
    print(i,end="") # prints each item in the count list on a new line

for i in count:
    print(i,end="\n") # prints each item in the count list on a new line

print("\n") # prints a new line

for i in count:
    print(i,end=" ") # prints each item in the count list on a new line

print("\n") # prints a new line

for i in count:
    print(i,end="\t") # prints each item in the count list on a new line

count=[0,1,2,3,4,5,6,7,8,9]

for i in range(len(count)):
    print(count[i],end="") # prints each item in the count list on a new line

if -1not in count:
    print("0 is not in the list")

count.append(-1) # adds -1 to the end of the count list

count.remove(-1) # removes -1 from the count list

count.insert(0,-1) # inserts -1 at index 0 of the count list



# Python list methods with examples

numbers = [3, 1, 4, 1, 5]

# append() - adds one item to the end
numbers.append(9)
print("append:", numbers)

# extend() - adds multiple items to the end
numbers.extend([2, 6])
print("extend:", numbers)

# insert() - inserts an item at a specific index
numbers.insert(1, 10)
print("insert:", numbers)

# remove() - removes the first matching item
numbers.remove(1)
print("remove:", numbers)

# pop() - removes and returns an item
last_item = numbers.pop()
print("pop:", last_item, numbers)

# pop(index) - removes an item at a specific index
removed_item = numbers.pop(1)
print("pop(index):", removed_item, numbers)

# clear() - removes all items
temporary = [1, 2, 3]
temporary.clear()
print("clear:", temporary)

# index() - returns the index of the first matching item
numbers = [3, 1, 4, 1, 5]
print("index:", numbers.index(4))

# count() - counts how many times an item appears
print("count:", numbers.count(1))

# sort() - sorts the list in ascending order
numbers.sort()
print("sort:", numbers)

# sort(reverse=True) - sorts the list in descending order
numbers.sort(reverse=True)
print("sort descending:", numbers)

# reverse() - reverses the list in place
numbers.reverse()
print("reverse:", numbers)


copied_numbers = numbers.copy()
print("copy:", copied_numbers)


# Useful list operations

values = [1, 2, 3]

# len() - returns the number of items
print("length:", len(values))

# min() - returns the smallest item
print("minimum:", min(values))

# max() - returns the largest item
print("maximum:", max(values))

# sum() - returns the total of numeric items
print("sum:", sum(values))

# in - checks whether an item exists
print("2 in values:", 2 in values)

# + - joins two lists
print("concatenation:", values + [4, 5])

# * - repeats a list
print("repetition:", values * 2)