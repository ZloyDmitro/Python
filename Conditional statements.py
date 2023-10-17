# Task 1

# user_input1 = int(input("Enter a First number: "))
# user_input2 = int(input("Enter a Second number: "))
# user_input3 = int(input("Enter a Third number: "))
# sum_of_numbers = user_input1 + user_input2 + user_input3

# if user_input3 == user_input2 == user_input1:
#     result = sum_of_numbers *3
#     print("First number:", user_input1)
#     print("Second number:", user_input2)
#     print("Third number:", user_input3)
#     print(" The sum is:", result)

# else:
#     print("First number:", user_input1)
#     print("Second number:", user_input2)
#     print("Third number:", user_input3)
#     print(" The sum is:", sum_of_numbers)

#Task2

# user_input1 = float(input("Enter a First number: "))
# user_input2 = float(input("Enter a Second number: "))
# difference_of_numbers = abs(user_input1 - user_input2)

# if user_input1 > user_input2:
#     result = difference_of_numbers *2
#     print("First number:", user_input1)
#     print("Second number:", user_input2)
#     print("The result of calculation is ", result)
# else:
#     print("First number:", user_input1)
#     print("Second number:", user_input2)
#     print("The result of calculation is ", difference_of_numbers)

# Task3 

# user_input1 = int(input("Enter a First number: "))

# if user_input1 % 2==0:
#     print("Number to check:", user_input1)
#     print(user_input1, "is an even number")
# else:
#     print("Number to check:", user_input1)
#     print(user_input1, "is an odd number")

from math import pi
user_input1 = float(input("Input the radius of the circle "))
r = user_input1
circle = (pi*r**2)
print("The area of the circle with radius", r, "is:", circle)
