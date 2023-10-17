string1 = "This is a string"
string1 = "12kl515"
# print(string1.capitalize())
# print(string1.upper())
# print(string1.lower())
# print(string1.isalpha())
# print(string1.isdecimal())
# print(string1.isdigit())
# print(string1.isalnum())
# print(string1.isnumeric())
# [I love Python too, and especially Python 3.x]
# text = "I love Python too, and especially Python 3.x"
# found = text.find("Python", 8)
# print("With the find method: ", found)

# found = text.index("Python", 8)
# print("With index Method", found)

# #split and replace
# text =  "I love Python too, and especially Python 3.x \nI also like other programming.\nFor instance, Java and C#."
# print(text)
# words = text.split("\n")
# print(words)
# #recreating the original text
# print("\n".join(words))
# # replace
# print(text.replace("Python", "Java"))

# # str.method
# print("String with a number using plus operator " +str(234))

##String Basics 1

# #Task1

# city = "London"
# print(city)
# Task1

# city = "berlin"
# population = 3645000
# city = city.capitalize()
# print(f" {city}: {population}")

# #Task 3
# city = "london"
# population = 9000000
# city = city.capitalize()
# print(f"City: {city} ({city.isalpha()})\n Population: {population}")

# ##Task 4
# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
# found = text.index("capital")
# found2 = text.find("capital")
# print("With index Method capital:", found)
# print("With found Method capital:", found2)

# # Task 5 
# text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
# words = text.split()
# print(words)

# #Task 6

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
# print(text.replace("capital","capital of Germany"))


## Task  len. length() in Python

# def detection(text):
#     letter_count = len(text)
#     if letter_count % 2 == 0:
#         print(f"{text} is even ")
#     else:
#         print(f"{text} is odd")
# text = input(f"Type a word or string:\n")
# detection(text)

## find in Python
## Task - Finding Nemo

# def find_nemo(text):
#     index = text.find("Nemo")
#     if index != -1:
#       print(f"I found Nemo at index {index}")
#     else:
#       print(f"I can't find Nemo :(")
# text = input(f"Type a word or string:\n")
# find_nemo(text)

# def replace(text):
#     find = text.find("dog")
#     if find != -1:
#         replaced_text = text.replace("dog", "cat")
#         print(replaced_text)
#     else:
#         print(f"There is no 'dog' in this text: {text}")

# text = input(f"Type a text what you want to replace with cat:\n")
# replace(text)
