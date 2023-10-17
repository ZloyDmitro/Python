# print(0b01) #1
# print(0b10)
# print(0b11)
# print(0b100)
# print(0b101)
# print(0b110)
# print(0b111)
# print(0b1000)
# print(0b1001)
# print(0b1010) #10

# print(bin(8)) # show binary represantation

# print(int("1000001", 16))

# a = 100
# b = 200

# if b > a:
#     print("b is greater than a")
# elif b == a:
#     print("b are equal to a")
# else:
#     print("a is greater than b")

# for x in range(1, 10, 2): #from 1 and till 10 but ends with 9, every second number
#     print(x)
# for x in range(11):
#     print(x)

# list = ["first", "second", "third", "fourth", "fifth"]
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in list:
#     if x == "fourth":
#         #break # or further to continue
#         continue
#     print(x)
# for y in list1: # here we can make loop inside loop
#         print(y)
# else:
#     print("The loop is finished..")

#pass Statements

# while loops      
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("loop is finished")

# x = 10
# while x >= 0:
#     print(x)
#     x -= 1
# x = 10
# while x >= 5: often in Games when no movement registered
#     print(x)
#     for y in range(10):
#         print ("inner loop", y + x)
#     x -= 1
# x = 10
# Same thing as while with for loop
# x = 5
# for x in range(5): #going through list
#     if x == 3:
#         continue   
#     print(x)
#     for y in range(10, 0, -1):
#         print("inner loop", y + x)
#     x -= 1
    

#Exercises 1
# x = 100
# print("binary format",(bin(x)))
# print("back in decimal format",(int(x)))
# print("back in hexadecimal format",(hex(x)))
# print("back in octal format",(oct(x)))

# extra Exercises 1

# for loop

# for i in range(3):
#     # Ask the user for a number
#     user_input = int(input("Enter a number: "))
    
#     # Check if the number is even or odd
#     if user_input % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")



# # Exercise 2 Initialize a variable to store the sum
# sum_of_numbers = 0

# # Use a for loop to iterate three times
# for i in range(3):
#     # Ask the user for a number and convert it to an integer5
#     user_input = int(input("Enter a number: "))
    
#     # Add the entered number to the sum
#     sum_of_numbers += user_input

# # Print the sum of the three numbers
# print("Sum of the three numbers:", sum_of_numbers)


# Initialize a variable to store the maximum number
# max_number = None

# Use a for loop to iterate five times
# for i in range(5):
#     # Ask the user for a number and convert it to an integer
#     user_input = int(input("Enter a number: "))
    
#     # Check if it's the first input or greater than the current maximum
#     if max_number is None or user_input > max_number:
#         max_number = user_input

# # Print the maximum number
# print("Maximum number:", max_number)

# # Ask the user for a number and convert it to an integer
# user_input = int(input("Enter a number: "))

# # Initialize a list to store the divisors
# divisors = []

# # Find the divisors by iterating from 1 to the user's number
# for i in range(1, user_input + 1):
#     if user_input % i == 0:
#         divisors.append(i)

# # Print the divisors

# # print("Divisors of", user_input, "are:", divisors)
# user_input = int(input("Enter a number: "))
# divisors = []

# for i in range(1, user_input + 1):
#     if user_input % i == 0:
#         divisors.append(i)

# print("Dividers of", user_input, "are", divisors )


# user_input = int(input("Enter a number: "))
# if user_input % 2 == 0 and user_input % 3 == 0:
#     print(user_input, "is even and divisible by 3.")
# else:
#     print(user_input, "is not even/or not divisible by 3,")
#task 6
# user_input = int(input("Enter a number: "))
# if user_input > 0 and user_input % 2 == 1 and user_input % 7 == 0:
#     print(user_input, "is positive, odd, and divisible by 7.")
# else:
#     print(user_input, "does not meet all specified conditions..")

