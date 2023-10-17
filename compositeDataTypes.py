# # Primitives Data Types

# string = "Ana"
# character
# integer = 2
# float
# bool = True

# none = None # nichts als nichts

#     car:"ford"
#     color="blue"
#     year= 1957

# # Composite / Compound Data Types
# Mutable object containing other values 	list or [] In Phython only list
# mutable object containing other values 	tuple or () In Phython only tuble
# Contains values that can be multiple types 	dict or {} In Phython only dict

# # dict (mapping Type)
# my_car={
#     'car': 'ford',
#     'color': 'blue',
#     'year': 1957
# ## ..... Sequence Type
# ## Lists are mutable
# my_list=[car, color, year, my_car]

# }
# print(my_list)
# ## Tuples immutable
# my_tuple=(1,2,3,"blue")

#  ## -------Set Types
#  # sets immutable
#  # unique, unindext, unordered
#  my_set={1,2,3,4,5}
# # frozen sets
# my_frozenset=frozenset({1,2,3,4,5}) Immutable

# # ---- Special Data Types
# # Files
# # Function
# # Classes


daniel_dict= {
    "firstname": "Daniel",
    "lastname": "Ziebart",
    "age": 41,
    "maried": True,
}
adress= {
    "street": "Sicherstr.",
    "strNumber": 2,
    "postcode": 52068,
    "city": "Köln"
}

dict = {"adress":adress, "daniel_dict":daniel_dict
        
}
print(dict["adress"]["city"])

