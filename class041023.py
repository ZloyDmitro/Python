# def hello_world():
#     return 123, 235, "Hello", 5

# x = hello_world()
# print(x)
# print(type(x))
# # anotherFunc()

# def printNames(name, surname, profession = "student"): # none default in first position
#     return f"Your name is {name} and your surname is {surname}. Im a {profession}!"
# x = printNames("Daniel", "Ziebart") #positional arguments
# print(x)
# y = printNames("Robert", "De Niro", "actor") # keyword arguments
# print(y)
# z = printNames("Anna", "Pereira")
# print(z)

# def addNumbers(numbers): # with the star* we can pack list with numbers one by one! 
#      nums = 0
#      for x in numbers:
#           nums += x
#      return nums     

# x = addNumbers(1,2,3)
# y = addNumbers(1,2,3,4,5,6) # dont work because of the given parameter
# z = addNumbers(26,56,84,96,14,12,45,23,26)
# print(x)
# print(y)
# print(z)
##unpacking of functional arguments i.e. unpacking collections
# def multiplyByTwo(*args):
#      multi = 0
#      for x in args:
#           multi += x
#      return multi
# mylist = [26,56,84,96,14,12]
# mm = multiplyByTwo(*mylist)
# print(mm)
# # #unpacking in general
# # mylist = [26,56,84,96,14,12]
# # v1, v2, v3, v4, v5, v6 = mylist
# # print(v6)
# def multiByTwo (*args):
#     multi=1
#     for x in args:
#         multi *= x
       
#     return multi 
# MyList=[4,2,3]
# mm=multiByTwo(*MyList)
# print(mm)


# packing and unpacking using kwargs or keywords arguments

# def fullName(name, surname):
#     return f"Name {name}, surname {surname}!"

# retVal = fullName(name="Daniel", surname ="Ziebart")
# print(retVal)

# def fullName(**kwargs):

#     return f"Your Name is: {kwargs['name']}, surname: {kwargs['surname']}, profession: {kwargs['profession']}!"

# retVal = fullName(name = "Daniel", surname = "Ziebart", profession ="")
# print(retVal)
# retVal2 = fullName(name = "Daniel", surname = "Ziebart", profession = "student")
# print(retVal2)

##EXERCISES
# #1
# def isEven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# def isOdd(x):
#     if x % 2 != 1:
#         return False
#     else:
#         return True
    
# print(isOdd(1), isEven(1))
# print(isOdd(657842), isEven(657842))
# print(isOdd(0), isEven(0))

##2       
# def getParity(number, parity_type):
#     if parity_type == "even":
#         if number % 2 == 0:
#             return True
#         else:
#             return False
#     elif parity_type == "odd":
#         if number % 2 != 0:
#             return True
#         else:
#             return False  
#     else: 
#         return "Parity indicated is unknown"
    
# print(getParity(-2,"odd"))
# print(getParity(2, "number"))
# print(getParity(1, "even")) 

##3 wrong
# import datetime
# def greet(name, date):
#     datetime.datetime = date
#     if date < datetime.time(12, 0, 0):
#         print(f"Good Morning, {name}")
#     else:
#         print(f"Good Afternoon, {name}")

# print(greet(name="John", date=datetime.datetime(2021, 5, 7, 11, 59, 59)))
# print(greet(name="John", date=datetime.datetime(2021, 5, 7, 12, 0, 1)))
        
        
##4
# list = [0, 2, 4, 5]
# multList = [[0, 2, 4, 5],[6],[0, 2, 4, 5, 1, 4, 3, 2]]
# def sumAll(*multList):
#     sum = 0
#     for sublist in multList:
#         for x in sublist: 
#             sum += x
#     return sum
# result = sumAll(*multList)
# print(result) 

##5
# word = str(input("Plese enter one or more words:\n"))
# def pig_latin(word):

# settings = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "whatever":"Ford",
#   "subsettings":[1,2,3,4],
#   "userprofile": {"username":"Daniel", "password": [1245, 'strong']}
#     }
# print(settings["subsettings"][-1])
# print(settings["userprofile"]["password"][-1])
# print(len(settings))


# settings2 = dict(name = "John", age = 36, country = "Norway")
# print(settings2["age"])
# print(settings2.keys())

# Dictionaries can ziped from two lists and create a dictionary with the dict() constructor:
# list_one = ["Key1", "Key2", "SecretKey", "Key3"]
# list_two = [123, 1517, "Secret", 256]
# my_new_dict = dict(zip(list_one, list_two))
# print(my_new_dict)
#my_new_dict = {'Key1': 123, 'Key2': 1517, 'SecretKey': 'Secret'}

# settings = {
# "title":"My original title"
# }
# print(settings)
# def change_site_title(settings):
#     settings["title"] = "A new fancy title"
    #settings.update({"title":"My original title"})
#     print(settings)
# change_site_title(settings)
# print(settings)
##One of Pauls
# # def change_site_title(newTitle):
# #     settings["title"] = newTitle
# #     #settings.update({"title":"My original title"})
# # print(settings)
# # change_site_title("A new fancy titel")
# # print(settings)

#Task2
# settings = {
# "title":"My original title"}

# default_settings = {
# "title":"My original title"}

# def get_title(dict = default_settings):
#     return dict["title"]

# def change_site_title(newTitle):
#     settings["title"] = newTitle

# print(get_title(settings))
# print(get_title())
# change_site_title("A new fancy title")
# print(get_title(settings))
# print(get_title())

#Task3
# settings = {
# "title":"My original title",
# "pages":[]
# }

# default_settings = {
# "title":"My original title",
# "pages":[]
# }

# def get_pages(settings = default_settings):
#     return settings["pages"]

# def add_page(pages, settings = default_settings):
#     settings["pages"].append(pages)


# home = {"title": "Home", "path": "/"}
# add_page(home)
# print(get_pages())
# print(get_pages(settings))
# about = {"title": "About", "path": "/about/"}
# add_page(about, settings)
# print(get_pages())
# print(get_pages(settings))

#Task4
# The user {first} {last} has the following pictures:
# common_header.png
# {user_picture1.png}
# {user_picture2.png}


#TASK5


def pig_latin(*args, **kwargs):
    def translate_word(word, suffix):
        vowels = "aeiou"
        if word[0].lower() in vowels:
            return word.capitalize() + suffix
        else:
            return (word[1:].capitalize() + word[0]).capitalize() + suffix


    suffix = kwargs.get("suffix", "ay")
    single = kwargs.get("single", False)

    translated_words = []

    for arg in args:
        words = arg.split()
        translated_sentence = [translate_word(word, suffix) for word in words]
        translated_words.extend(translated_sentence)

    if single:
        return " ".join(translated_words)
    else:
        return translated_words
    
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

result1 = pig_latin(*test1_data, **test1_config)
result2 = pig_latin(*test2_data, **test2_config)
result3 = pig_latin(*test3_data, **test3_config)

print(result1)
print(result2)
print(result3)

# def pig_latin(*args, **kwargs):
#     def translate_word(word, suffix):
#         vowels = "aeiou"
#         if word[0].lower() in vowels:
#             return word.capitalize() + suffix
#         else:
#             return word[1:].capitalize() + word[0] + suffix

#     suffix = kwargs.get("suffix", "ay")
#     single = kwargs.get("single", False)

#     translated_words = []

#     for arg in args:
#         words = arg.split()
#         translated_sentence = [translate_word(word, suffix) for word in words]
#         translated_words.extend(translated_sentence)

#     if single:
#         return " ".join(translated_words)
#     else:
#         return translated_words

# # Test cases
# test1_data = ["Word", "Apple"]
# test1_config = {}

# test2_data = ["Python", "Functions"]
# test2_config = {"suffix": "oy"}

# test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
# test3_config = {"single": True, "suffix": "ep"}

# result1 = pig_latin(*test1_data, **test1_config)
# result2 = pig_latin(*test2_data, **test2_config)
# result3 = pig_latin(*test3_data, **test3_config)

# print(result1)
# print(result2)
# print(result3)


# def pig_latin(*args, suffix='ay', single=False):
#     # print(*args, suffix, single)
#     vowels = 'aeiou'
#     results =[]
        
#     for phrase in args:
#       for word in phrase.split(' '):
#         # print(word)
#         if word[0].lower() in vowels:
#             new_word=word+suffix
#             results.append(new_word)
#         else: 
#             new_word = word[1:]+word[0]+suffix
#             results.append(new_word)
#     if single: 
#         return(' '.join(results))
#     return(results)
        
        
        
# # Test cases
# test1_data = ["Word", "Apple"]
# test1_config = {}

# test2_data = ["Python", "Functions",]
# test2_config = {"suffix": "oy"}

# test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
# test3_config = {"single": True, "suffix": "ep"}

# print(pig_latin(*test1_data, **test1_config))
# print(pig_latin(*test2_data, **test2_config))
# print(pig_latin(*test3_data, **test3_config))

# table = [
  
#    ["string1", "string2", "string3"],
#     [1, 2, 3, 4, 5],
#     [True, True, False]
# ]
# print(table[2,][0:2])


# list1 = ["Guitars", "Drums", "Basses", "Trumpets"]

# # print(list1[-2:]) #shows us last 2 strings
# # print(list1[::-1]) #reverse the order of list
# # print(list1[::2]) #shows us every second string
# # print(list1[0:2]) 
# list1.reverse()
# print(list1)
# list1.sort(reverse=True) #with reverse=True we can sort in decending order
# print("The effect of using sort method on a list:", list1)


# list2 = [123,345,677]
# list2[0:2] = {444, 475}
# list2.extend([555])
# list2.append(559)
# list2[0:2] = [558]
# list2[0] = []
# print(list2)

# ourstring = "Lets use a split method again"
# print(ourstring.split(" "))

#tables
# list3 = [
# ["Heading1", "Heading2", "Heading3"],
# [123, 456, 678],
# [333, 555, 777]
# ]
# # print(list3[:])
# # print(list3[0:2][0:2])
# print("Two dimensional list using statement: \n,", list3)

import numpy as np

# mylist = np.array(list3)
# print("Two dimensional list using nparry: \n", mylist)


# twocollums = mylist[:, 0:2]
# print(twocollums)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))


# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print ("Number of diemesions :", arr.ndim)
# arr = np.array([1, 2, 3, 4])
# print(arr[0])
# print(arr[2] + arr[3])
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1]) 

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1,1,-1]+arr[1,1,-1])
# print(arr[1,1,:2])
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[::2])

# arr = np.array([1, 2, 3, 4], dtype='S')
# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype) 
# arr = np.array([1.9, 2.8, 3.5, 4, 5, 6, 7])

# new_var = arr.astype('i')
# print(new_var)