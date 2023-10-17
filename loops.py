# For loops
# my_list=[1,2,3, "Jeremiaj", "Kwane",{"Name":"Anna","age":41}]
                                     
# my_dict={

#     "name":"Daniel",
#     "age":41,
#     "location":"Hamburg"
# }

# print(my_list)
# print(my_list[-1]["Name"], my_list[-1]["age"])

#for looping through a list

# for i in my_list:
#     print(i)

# print(my_dict["location"])

# for looping through a dict

# for key,value in my_dict.items(): #keys are "name:Daniel in the dict" value is Daniel
#     print({value,key})

users=[
    {
        "name":"Daniel",
        "lastName":"Ziebart",
        "age":41,
        "hasCoffee": True
    },
    {
        "name": "Sami",
        "lastName": "Aiyob",
        "age": 30,
        "hasCoffee": True
    },
    {
        'name':'Etleva',
        'lastName': 'Sefaj',
        'age': 38,
        'hasCoffee': False
    },
    {
        'name':'Mhd Ammar',
        'lastName':'Nammour',
        'age':32,
        'hasCoffee': False
    },
    {
        'name': 'Aj',
        'lastName': 'Michael',
        "age": 17,
        'hasCoffee': True
}
]
# for i in users:
#     #print(i)
#     #for loop for dict
#     for key,value in i.items():
#         if key == "age":
#             if value <= 18:
#                 print(f"You'r {key} is {value}, you are NOT ready to drink!")


# def func1(list):
#     for user in list:
#         age = user["age"]
#         name = user.get("name")
#         if age <=18:
#             print(f"{name} you are NOT ready to drink, you are only {age}")
    
# func1(users)

# def func2(list):
#     for user in list:
#         hasCoffee = user["hasCoffee"]
#         name = user.get("name")
#         if hasCoffee == True:
#             print(f"{name} you are good person!")
#         else:
#             print(f"{name} you will be efficient, when you drink Coffee!")
    
# func2(users)
            
# def func2(list):
#     input_name = input("Plese tell me your name! ")
#     for user in list:
#         hasCoffee = user["hasCoffee"]
#         name = user.get("name")
#         if input_name == name:
#             hasCoffee == True
#             print(f"{name} you are good person! ")

    
func2(users)

#While loops

temp= int(input("What is the temp? "))
while temp<20:
    temp +=1
    if temp >= 20:
        print(f"Heating on temp {temp}")

while temp>25:
    temp -=1
    if temp >= 20:
        print(f"Turn on air conditioner {temp}")
