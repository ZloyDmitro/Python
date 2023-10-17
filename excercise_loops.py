temp= int(input("What is the temp? "))
while temp<20:
    temp +=1
    if temp >= 20:
        print(f"Heating on temp {temp}")

while temp>25:
    temp -=1
    if temp >= 20:
        print(f"Turn on air conditioner {temp}")



while True:
    temp = int(input("Provide the temperature: \n"))
    if temp <= 20:
        print(f"Turn on the aircondition with {temp}!")
        continue
    elif temp >= 25:
        print(f"The airconditioner ist on ... The programm will quit now!")
        break

x = 0
y = 1

while x < 100:
    print(x)
    x, y = y, x + y

fibonacci = [0,1]

while fibonacci[-1] + fibonacci[-2] < 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)

#Task 1 - multiplication table

num = int(input("Enter a number to generate its multiplication table (1 to 10): "))

if 1 <= num <= 10:
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        product = num * i
        print(f"{num} x {i} = {product}")
else:
    print("Please enter a number between 1 and 10.")

#Task 2 - pattern with loop
num_rows = 9

for i in range(1, num_rows + 1):
    for j in range(i):
        print(i, end="")
    print()

word = (input("Enter one word to reverse it: "))
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print("Reversed word:", reversed_word)

#Task 4 - upper letters

text = (input("Enter one text to change o with O: "))
for i in text:
    new_text = text.replace('o', 'O')
    print(new_text)
    break

#Task 5 - count digits and letters
digit_count = 0
letter_count = 0
text = (input("Enter one word to count all digits and letters: "))
for char in text:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print("Numbers of digits:", digit_count)
print("Numbers of letters:", letter_count)

# while loops 
# Task1 omitting number

num = -5
while num <= 5:
    if num != 0:
        print(num)
    num += 0.5
   
# Upper and lower letters
text = (input("Enter one text to converts the lower letters to capital letters and vice versa: "))
new_text = ""
i = 0
while i < len(text):
    char = text[i]
    if char.islower():
        new_text += char.upper()
    elif char.isupper():
        new_text += char.lower()
    else:
        new_text += char
    i += 1
print(new_text)

Task 3 average of numbers
total = 0
count = 0
while True:
    try:
        num = int(input(f"Enter various whole numbers to calculate the average of numbers, 0 to finish:\n"))
        if num == 0:
            break
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")
if count == 0:
    print("No numbers were entered.")

else:
    average = total / count
    print(f"The average of {count} numbers is: {average}")

# Task 4 find a character

text = input("Please give me a Text to find an index of given Character:\n")
letter_to_find = input("Which letter i have to find?\n")
index = 0
indexes = []
while index < len(text):
    index = text.find(letter_to_find, index)
    if index == -1:
        break
    indexes.append(index)
    index += 1

if indexes:
    print(f"The character {letter_to_find} was found at indexes: {indexes}")
else: 
    print(f"The character {letter_to_find} was not found in the text.")

Task 5 - find divisible numbers


while True:
    try:
        start = int(input("Type start integer: "))
        end = int(input("Type end integer: "))
        divisor = int(input("Type divisor: "))
        
        if divisor == 0:
            break
        
        current = start
        
        while current <= end:
            if current % divisor == 0:
                print(f"{current} is divisible by {divisor}")
            current += 1
        
    except ValueError:
        print("Invalid input. Please enter integers for start, end, and divisor.")

print("Program finished.")