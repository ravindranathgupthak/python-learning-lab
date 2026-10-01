
# Exercise 02: Data Structures

# Create a list and print it. Ordered collection of items,
# allows duplicate values.
alist = ["apple", "banana", "cherry"]
print(alist)
print(len(alist)) # length of the list

# Create a tuple and print it. Ordered collection of items, 
# allows duplicate values, but is immutable.
atuple = ("apple", "banana", "cherry", "apple")
print(atuple)
print(len(atuple)) # length of the tuple

# Create a set and print it.
# unordered collection of unique items, duplicate values are removed.
aset = {"apple", "banana", "cherry", "apple"}
print(aset)
print(len(aset)) # length of the set

# Create a dictionary and print it. Unordered collection of key-value pairs,
# keys are unique, values can be duplicate.
adict = {"name": "John", "age": 30, "city": "New York", "age": 25}
print(adict)
print(len(adict)) # length of the dictionary