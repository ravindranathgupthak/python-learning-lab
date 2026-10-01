# Exercise 03: lists

# Create a list of languages names
languages = ["Python", "C", "C++", "Rust", "Java"]

# print entire list of languages
print("List of languages:", languages)

# print first language in the list
print("first language in the list:", languages[0])

# print last language in the list
print("last language in the list:", languages[-1])

# print number of languages in the list
print("No. of languages in the list :", len(languages))

# length of the list using __len__ method
print("no of languages using __len__():", languages.__len__())

# add another language to the list
languages.append("JavaScript")
print("list of languages after appending new lang:", languages)

# insert a new languages at index 2
languages.insert(2, "Go")
print("list of languages after inserting new lang at index 2:", languages)

# Remove one language from the list
# remove() method removes the first matching value, not a specific index.
# If the value is not found, it raises a ValueError.
languages.remove("Java")
print("list of languages after removal of a language:", languages)

# Remove the last element using pop() and print the element that was removed
# pop() method use an index as an argument to remove a specific element from the list.
# if no index is provided, it removes the last element from the list.
removed_language = languages.pop()
print("list of languages after pop():", languages)
print("removed language:", removed_language)

# Check whether "Python" exists in the list using in.
if "Python" in languages:
    print("Python exists in the list")
else:
    print("Python doesn't exist in the list")

# print every language in the for loop
print("All languages in the list:")
for language in languages:
    print(language)

# Print the first three elements using list slicing.
print("first 3 languages in the list:", languages[:3])

# Sort the list alphabetically and print it.
languages.sort()
print("Sorted list of languages:", languages)

# Reverse the list and print it.
languages.reverse()
print("Reversed list of languages:", languages)

# Sort the list in reverse alphabetical order and print it.
languages.sort(reverse=True)
print("Sorted list of languages in reverse order:", languages)

# Bonus items on lists exercise:
numbers = [45, 12, 89, 34, 67, 23, 91, 56]

print(numbers)
# Print the minimum, maximum and sum of the numbers in the list.
print("smallest number in the list:", min(numbers))
print("largest number in the list:", max(numbers))
print("sum of numbers in the list:", sum(numbers))
# Calculate the average of the numbers in the list and print it.
print("Average of numbers in the list:", sum(numbers) / len(numbers))

# Challenge: Find the second-largest number in the list without sorting it.
print(numbers)
if len(numbers) >= 2:
    largest = None
    second_largest = None
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is not None:
        print("Second largest number in the list:", second_largest)
    else:
        print("There is no second largest number in the list.") 

# list with mixed data types
alist = [1, "apple", 3.14, True]
print(alist)

# Create a nested list and print it.
nested_list = [1, 2, ["apple", "banana"], 3.14, True]
print(nested_list)
print("Length of the nested list:", len(nested_list))
print("Third element of the nested list:", nested_list[2])