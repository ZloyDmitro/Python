# Methods Vs Functions
# - tied to an object(instance)
#Math.min([1,2,3,4,5,6])

# # Function
# def my_func():
#     print("Hello World")

# my_func()

# def your_func():
#     print("llts make it")

# your_func()

# List Methods
# Python has a set of built-in methods that you can use on lists.
# Method 	Description
# .append()	Adds an element at the end of the list
# .clear()	Removes all the elements from the list
# .copy()	Returns a copy of the list
# .count()	Returns the number of elements with the specified value
# .extend()	Add the elements of a list (or any iterable), to the end of the current list
# .index()	Returns the index of the first element with the specified value
# .insert()	Adds an element at the specified position
# .pop()	Removes the element at the specified position
# .remove()	Removes the item with the specified value
# .reverse()	Reverses the order of the list
# .sort()	Sorts the list

python_2023 = ["James", "Robert", "John", "Michael", "David"]
unsorted = [25,15,46,748,45,84,92,1,56,26,34,16,58,22,88]
# python_2023.append("Marcel")
# print(python_2023)
# # Remove
# python_2023.remove("Marcel")
# print(python_2023)
# #sort
python_2023.sort()
print(python_2023)
unsorted.sort()
unsorted.count()

print(unsorted.pop(0))