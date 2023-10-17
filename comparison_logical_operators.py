# # Python Introduction

# ## Comparison and logical operators

# In this exercise, we will focus on the usage of the comparison and logical operators, including:  
#  - equal operator `==`,
#  - not equal operator `!=`,
#  - greater than operator `>`,
#  - less than operator `<`,
#  - greater than or equal to operator `>=`,
#  - less than or equal to operator `<=`,
#  - `and`, `or`, `not` logical operators, 
#  - using `None`.

# ## 

# ## Tasks

# ### 

# ### :heavy_plus_sign: Task 1 - comparison operators

# Your task is to write a program which asks the user three times about two integer numbers to compare. 
# >Hint: Use `while` loop to perform the same operation more than once!  

# Use both comparison and logical operators, for example use logical comparison between two or more comparion operators:  
# >Example: 
# ```python
# result = None
# if (expression1) and (expression2):
#     print(information)
# ```
# Create **at least ten** comparisons!  

# - Some of your results could look like this:

# ```bash
# Enter first number: 1234
# Enter second number: 5432
# Numbers are not equal
# Second number is greater than first number
# Second number is greater than or equal to first number
# Both numbers are big!
# big_numbers is set to  True

# Enter first number: 23
# Enter second number: 4567
# Numbers are not equal
# Second number is greater than first number
# Second number is greater than or equal to first number
# Both numbers are not big!
# big_numbers is set to  False
# ```

# ### :heavy_plus_sign: Task 2 - convertion month name to a number of days

# Your task is to write a Python program to convert month name to a number of days. 
# >Hint: Print list of months at the beginning.  

# User should be prompted to enter name of the month and the output shoul be the number of days in given month.

# - Some of your results could look like this:

# ```bash
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of Month: May
# Number of days: 31 days
# ```

#Class
# logical and, or, not
# x = 9
# age = 18
# if x == 10 or age == 18:
#     print("You are welcome ond our platform")
# else:
#     print("sorry, not all conditions were met!")

# # oneline
# print("Yes, good") if not(x == 10 and age == 18) else print("sorry, not possible")


# def add_numbers(num1, num2):
#     user_input = int(input("Enter a number: "))
#     sum = num1 + num2
#     print("Sum: ", sum)
#     return sum

#functions

# def myfunction():

#     print("this is my first function!")
#     print("bla bla bla")
#     print("to to to to you")

# myfunction()
# myfunction()

# funcTest = myfunction()
# print(funcTest)

# funciton with a return keywords

# def power(x, y):
#     z = x**y
#     return z
# arg1 = input("Enter a first number")
# arg2 = input("Enter a second number")
# result = power(float(arg1), float(arg2))
# print(result)


# hobby1 = input("please specify your favourite hobby: ")
# hobby2 = input("please specify your second hobby: ")
# hobby3 = input("please specify your third hobby: ")
# holidays = input("Please specify the number of days used for hobbies last year")

# print(hobby1)
# print(hobby2)
# print(hobby3)
# def displaySeparators():
#     print("+++++++++++++++++++++++++")

# def managehobbies(hobby1, hobby2, hobby3, holidays):
#     costOfHolidaysPerDay = 300
#     displaySeparators()
#     print("My favourite hobby is:", hobby1)
#     print("My second favourite hobby is:", hobby2)
#     print("My third favourite hobby is:", hobby3)
#     cost = int(holidays) * int(costOfHolidaysPerDay)
#     print("I spend: " + holidays + "days doing may hobby last year.")
#     print("The cost of my hobby last year was", cost)
#     displaySeparators()
#     return cost

# costOfHobbies = managehobbies(hobby1, hobby2, hobby3, holidays)
# print("The cost of my hobby last year was:" + str(costOfHobbies) + " and this year the cost of might be ", + (costOfHobbies)*1.2)


# user_name_input = input("What is your user name? ")
# user_age_input = int(input("What is your age? "))

# def user_information(user_name, user_age):
#     full_information = (f"Your {user_name} and your age is {user_age}")
#     return full_information 

# summary = user_information(user_name_input, user_age_input)

# print(summary)

# def get_user_information():
#     while True:
#         try:
#             user_name = input("What is your user name? ")
#             user_age = int(input("What is your age? "))
#             return user_name, user_age
#         except ValueError:
#             print("Invalid age. Please enter a valid numeric age.")

# def format_user_information(user_name, user_age):
#     return f"Your name is {user_name} and you are {user_age} old."

# if __name__ == "__main__":
#     user_name, user_age = get_user_information()
#     summary = format_user_information(user_name, user_age)
#     print(summary)

#Exercises
# Task 1 Your task is to write a program which asks the user three times about two integer numbers to compare.

# big_numbers = False

# # Loop three times to ask for input
# for i in range(3):

#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
    
#     if first_number !=  second_number:
#         print("Numbers are not equal")
#     elif second_number >= first_number:
#         print("Second number is greater than first number")
#         print("Second number is greater than or equal to first number")
#     else:
#         second_number <= first_number
#         print("Numbers are equal")
#         print("First number is greater than second number")
#         print("First number is greater than or equal to second number")
    
#     if first_number >= 1000 and second_number >= 1000:
#         big_numbers = True
#         print("Both numbers are big!")
#     else:
#         print("Both numbers are not big!")

# if big_numbers:

#     big_numbers = True
# else:
#     print("Not both numbers are big.")

# print(f"big_numbers is set to {big_numbers}")

#Task 2 Your task is to write a Python program to convert month name to a number of days.

month_to_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

user_month = input("Enter the name of a month: ")

user_month = user_month.strip().title()

if user_month in month_to_days:
   
    days_in_month = month_to_days[user_month]
    print(f"The number of days in {user_month} is {days_in_month}.")
else:
    print("Invalid month name. Please enter a valid month name.")

        
