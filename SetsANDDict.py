from pprint import pprint
# set1 = {"Apples", "Carrots", "Oranges", 1, 1, 15}
# set1.add(15)
# set1.add(True)
# set1.add(False)

# #print(hash(set1)) sets can not be hashed because changeble
# #Please do not use pop() with sets.
# set1.remove(1)
# set1.discard("Oranges") # is safer than remove() method
# #update Method accepts a list and does a job of an add method using multiple values
# set1.update(["Random value", 16, 18, 90])

# print(set1)

##Use cases for two or more sets of data
#set1 = {"Fender", "Peavey", "Gibson", "Marshall", "Ibanez", "Boss", "Peavey"}
#set2 = {"Fender", "Boss", "Peavey"}
#set3 = {"Fender", "Boss", "Peavey"}
#print(set1.intersection(set2))
#print(set1)

# ## check for content equaly
# print("Checking for set content equality: ", set2 == set3)
# print("Checking for reference equality: ", set2 is set3)

## Show unique elements of one set wich difference
#print(set1.difference(set2))
## Show non common elements of both sets.
#print(set1.symmetric_difference(set2))
##show everything or two sets.
#print("Union of tho sets: ", set1.union(set2))
## testeing sets using precicate methods
# print("Checking for disjoints: ", set1.isdisjoint(set2))
# print("Checking for subset: ", set1.issubset(set2))
# print("Checking for superset: ", set1.issuperset(set2))
# for x in set1:
#     print(x)
##DICT

# students = {
#     "student1": {
#         "name": "Daniel",
#         "surname": "Ziebart",
#         "profession": "Programmer",
#         "languages": ["Python", "Java", "C#", "Java"],
#         "drinks": {
#             "coffee": "Cafe Latte",
#             "beer": "Becks",
#             "wine": "Pinot"
#         }
#     },
#     "student2": {
#         "name": "Paul"
#     },
#     "student3": {
#         "name": "Daniel"
#     },
#     "student4": {
#         "name": "Sami"
#     }
# }

# print(students["student1"]["languages"])
# dict = {}

# dict2 = dict.fromkeys(("name", "surname", "profession"), {"k": "Default values"})
# print(dict2)

# dict1 = {
#             "coffee": "Cafe Latte",
#             "beer": "Becks",
#             "wine": "Pinot"}

# for key in dict1:
#     print(key, dict1[key])

# for key, value in dict1.items():
#     print(key, value)

# for value in dict1.values():
#     print(value)

# fruits = {
#   'red': ['apple', 'cherry', 'strawberry'],
#   'orange':['orange', 'mango', 'peach'],
#   'yellow': ['banana', 'lemon']
# }
# # adding new element to dict
# fruits["green"] =["watermelon"]
# fruits.update({"black": ["cherry", "currant"]})
# fruits.pop("black")

# # loop inside loop for searching in list an display
# for key, value in fruits.items():
#     for x in value:
#         print(x)


##Task1
# person = {
#     "name":"Bart Simpson",
#     "adress":"742 Evergreen Terrace"
# }
# print(person["name"]+",",person["adress"])

##Task2
# bart = {
#     "name":"Bart Simpson"
# }
# homer = {
#     "name":"Homer Simpson"
# }
# adress = {"adress":"742 Evergreen Terrace"
# }
# bart.update(adress)
# homer.update(adress)
# print(bart["adress"])

##Task3
# ages = {
#     "Peter":36,
#     "Robin":29,
#     "Michael":33
# }
# for key, value in ages.items():
#     print(key+" is "+str(value)+" years old")

##Task4
# zoo = {"Alligator":10,
#        "Tiger":4,
#        "Parrot":100,
#        "Hamster":50,
#        "Dolphin":15
#        }
# animals_to_remove = []
# for animal in zoo:
#     if animal[-1] == "r":
#         animals_to_remove.append(animal
#                                  )
        
# for animal in animals_to_remove:
#     del zoo[animal]
    
# for animal, count in zoo.items():
#     print(animal, count)
##Task with Harry Potter
books = {
    'Harry Potter And The Sorcerer\'s Stone': 1241100000,
    'Harry Potter And The Chamber Of Secrets': 771300000,
    'Harry Potter And The Prisoner Of Azkaban': 65210000,
    'Harry Potter And The Goblet Of Fire': 645600000,
    'Harry Potter And The Order Of The Phoenix': 635600000,
    'Harry Potter And The Half Blood Prince': 661300000,
    'Harry Potter And The Deathly Hallows': 652200000,
}

sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)[:3]
for book, sales in sorted_books:
  print(f"{book}: {sales}")



# def get(data, path):
#     segments = path.split('.')
#     current_data = data
#     for segment in segments:
#         if segment.isdigit():
#             current_data = current_data[int(segment)]
#         else:
#             current_data = current_data.get(segment)
#         if current_data is None:
#             return None
#     return current_data
# print(get(data, 'students.1.subjects.0.name'))
# print(get(data, 'students.0.subjects.0.teacher'))
# print(get(data, "students.0.subjects.0.name"))
# pprint(data)

# data = {
#   'students': [
#     {
#       'name': 'Josephine',
#       'subjects': [
#         {
#           'name': 'English',
#           'teacher': 'Mr. Hoover'
#         }
#       ]
#     },
#     {
#       'name': 'Luke',
#       'subjects': [
#         {
#           'name': 'History',
#           'teacher': 'Mrs. Peters'
#         }
#       ]
#     },
#     {
#       'name': 'Julia',
#       'subjects': [
#         {
#           'name': 'Chemistry',
#           'teacher': 'Mrs. Fauci'
#         }
#       ]
#     }
#   ]
# }
# print(data['students'][0]["subjects"][0]["teacher"])
# print(data['students'][1]["subjects"][0]["teacher"])
# print(data['students'][2]["subjects"][0]["teacher"])
# pprint(data['students'][0]["name"])

# print(data.get("teacher", "Nothing found"))
# print(data)

##Task - Maths with dictionary elements

# dict1 = {
#   'a': 4,
#   'b': 16,
#   'c': 3
# }
# dict2 = {
#   'a': 8,
#   'b': 2,
#   'c': 3
# }
# result = 0
# for key in dict1:
#     if key in dict2:
#         result += dict1[key]*dict2[key]

# print(result)
# result = dict1["a"]*dict2["a"]+dict1["b"]*dict2["b"]+dict1["c"]*dict2["c"]
# print(result)

# natural_case = {
#   'Company name': 'Digital Career Institute',
#   'Street': 'Vulkanstraße',
#   'House Number': 1,
#   'City': 'Berlin'
# }
# natural_case = {
#   'Movie name': 'James Bond 007: Skyfall',
#   'Director': 'Sam Mendes',
#   'Production Year': 2012,
#   'Duration in minutes': 143,
#   'Production countries': ['US', 'UK']
# }

# snake_case = {}
# for key, value in natural_case.items():
#    split_key = key.split(" ")
#    snake_key = "_".join([word.lower() for word in split_key])
#    snake_case[snake_key] = value
# print("snake_case = {\n", snake_case)
#pprint("snake_case = {\n", snake_case)

##Task - Combine lists into a dict
# color_names = ['red', 'green', 'blue']
# color_hex = ['#FF0000','#00FF00', '#0000FF']
# colors = {}
# colors_update = zip(color_names, color_hex)
# colors.update(colors_update)
# print(colors)
# pprint(colors)
# colors = {'blue': '#0000FF', 'green': '#00FF00', 'red': '#FF0000'}

##Task - Matrix mean
# numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
# def mean(sublist):
#     mean_values = []
#     for sublist in sublist:
#       total = sum(sublist)
#       mean = total / len(sublist)
#       mean_values.append(round(mean))
#     return mean_values
# result = mean(numbers)
# print(result)

