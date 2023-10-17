#assiging funciton delaration (header) to a variable
# def simpleFunc():
#     return "I a simple function"

# retVal = simpleFunc
# print(retVal) #die Function der Funktion wird hier gespeichert und kann als variable verwendet werden
# print(retVal())


# def wrapper(func):
#     print(func)

# wrapper(retVal)

#Nestet Function

# def outer_funciton():
#     x = 10
#     def inner_funciton():
#         print("I am an inner function")
#     inner_funciton()

# outer_funciton()


#inner_function() #not defined outside the function

# #returning a funciton from a funciton
# def outer_funciton():

#     def inner_funciton():
#         return "I am an inner function"
    
#     return inner_funciton

# recievedFunction = outer_funciton()
# print(recievedFunction)
# print(recievedFunction())

#Closure

# def outer_funciton(x):

#     def inner_funciton():
#         return "I am an inner function " + str(x)
    
#     return inner_funciton

# recievedFunction = outer_funciton(1234)
# print(recievedFunction)
# print(recievedFunction())


#DECORATOR design pattern:
#1. nested function
#2. return an innerfunction from the outer funciton
#3. pass a funciton to an outer funciton
#4. execute a passed function within the inner function
#5. profiede some usefull funcitonlity before or after executing a passed funciton
# This usefull functionality is known as a decoration

# def helloDec():
#     return "Hello Decorators!"

# def outer_funciton(func):

#     def inner_funciton():
#         print("This is my decoration before executing passed function...")
#         message = func()
#         print(message)
#         print("This is my decoration after executing passed function...")
#         return "I am an inner function"
        
    
#     return inner_funciton


# recievedFunction = outer_funciton(lambda: "I want to be a decorator")
# print(recievedFunction)
# print(recievedFunction())