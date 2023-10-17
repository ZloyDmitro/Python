#add values to a list
list1 = ["Tomatoes", "Potatoes", "Cucumbers", "Onions", "Beer"]
#print(list1)
# list1.append("Soda")
# #print(list1[-2:])
# list2 = ["Wine", "Vodka"]
# list3 = list1 + list2
# #print(list3)

# list3.insert(1, "Apples")
# print(list3)
# list3.pop()
# print(list3)
# list3.pop(1)
# print(list3)
# list3.remove("Soda")
# list5= ['Tomatoes', 'Apples', 'Potatoes', 'Cucumbers', 'Onions', 'Beer', 'Soda', 'Wine', 'Vodka']
# list6= ['Tomatoes', 'Apples', 'Potatoes', 'Cucumbers', 'Onions', 'Beer', 'Soda', 'Wine', 'Vodka']

# print(list5 == list6) # compares values inside the lists, have to be identical in content and position

# if list5 is list6: #compares memory adress of lists
#     print("The lists have the same adress: ", id(list5))
# else:
#     print("Both list have different adress: ", id(list5), id(list6))

#print(list5 == list6[::-1])
# list7 = list6.copy() # give a new copy a neu adress
# print(list7)
# list7.clear() # empty the list
# print(list7)
# del list7 # complietly delete the list.
# print(list7)

# tuple1 = (1,2,3,"String", False, [0,2,4])
# list1 = [2,4,5, True, False, True, "String", "String", 2, 5, (12, 1, 88)]
# print(tuple1)
# tuple2 = tuple("A String that will be turned into a tuple...")
# print(tuple2)
# print(tuple1[-1][-1])

# convertation between a tupple an a list
# tuple3 = tuple(list1)
# print(tuple3)

# list2 = list(tuple3)
# print(list2)
# print(tuple3.index(True, 4))
# print(tuple3.count(2))
# print(len(tuple3)) # count an return all elements in a tuple

# #To check unique values

# uniqueValues = set(tuple3)
# print(uniqueValues)
# print(len(uniqueValues))
# print(" There are " + str(len(uniqueValues)) + " unique, non-dublicated values")


# tuple4 = ([1,2,3], [2,3,4])
# print(tuple4)

# single = (2, 3, 5)
# single1 = (2, 3, 5)
# print(type(single))
# print(single1 is single)

# #list unpacking
# list1 = ("list1", "list2", "list3")
# var1, var2, var3 = list1
# print(var2)

# #swap two variables

# simpleTuple = (3,6)
# x, y = simpleTuple
# newTuple = (y, x)
# print(newTuple)

# x, y = y, x
# print(x, y)

# #in keyword
# if "list1" in list1:
#     print("A number exist in a collection")
# else:
#     print("The varialbe ist not in a collecton")
#Collections Basics
#Tasks1
# fruits = []
# fruits.insert(0,"Apples")
# print(fruits[0])
# fruits.insert(1,"Cherries")
# print(fruits[1])
# fruits.insert(2,"Strawberries")
# print(fruits[2])

#Tasks2
# cities = ["London", "Paris", "Berlin", "Amsterdam"]
# print(f"The capital city of Germany is: {cities[2]}")

#Tasks3
# colors = ["cyan", "magenta", "green", "yellow", "black", "white"]
# colors.pop(2)
# print(colors)
# colors.remove("white")
# print(colors)

#Tasks4
# word = ["p", "e", "n", "g", "u", "i", "n"]
# word1 = "".join(map(str, word))
# word1 = word1.capitalize()
# print(word1)
##Task - Swap list elements
# swap_list = [23, 65, 19, 90]
# swap_list[1], swap_list[3] = swap_list[3], swap_list[1]
# print(swap_list)

# def swap(input_list, index1, index2):
#     if 0 <= index1 < len(input_list) and 0 <= index2 < len(input_list):
#         input_list[index1], input_list[index2] = input_list[index2], input_list[index1] 

# swap_list = [23, 65, 19, 90]

# swap(swap_list, 1, 3)
#Task - Filter lists
# def digit_filter(input_list):
#     filterdList = [x for x in input_list if x.isalpha()]
#     return filterdList

# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
# filteredresult = digit_filter(l33t)
# print(filteredresult)

#Task - Unique sort
# def unique_char_count(s):
#     return len(set(s))

# def unique_char_sort(input_list):
#     sorted_list = sorted(input_list, key=unique_char_count)
#     return sorted_list

# strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']
# sorted_result = unique_char_sort(strings)
# print(sorted_result)
# import string

# def is_pangram(input_string):
#     input_string = input_string.lower()
#     alphabet_set = set(string.ascii_lowercase)
#     return set(input_string) >= alphabet_set

# user_input = input("Enter a string: ")

# result = is_pangram(user_input)

# if result:
#     print("The input is a pangram.")
# else:
#     print("The input is not a pangram.")


 
# def ispangram(str):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str.lower():
#             return False
 
#     return True
     
# string = "Pack my box with five dozen liquor jugs."
# if(ispangram(string) == True):
#     print("The input is a pangram.")
# else:
#     print("The input is not a pangram.")

#Task - List intersection

# def intersection(list_1, list_2):
#     result = []
#     for x in list_1:
#         if x in list_2:
#             result.append(x)
#     return result
# list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# list_3 = set(intersection(list_1, list_2))
# list_3 = list(list_3)
# print(list_3)
