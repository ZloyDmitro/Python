Task1
add15 = lambda x: 15 + x
print(add15(1))
print(add15(-2))

Task2
isOdd = lambda x: x % 2 != 0
isEven = lambda x: x % 2 == 0
getParity = lambda x, y: True if x % 2 == 0 and y == "even" else False if x % 2 != 0 and y != "odd" else True if x % 2 != 0 and y == "odd" else False if x % 2 == 0 and y == "odd" else None
print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))

TASK3
starts_with_p = lambda x: True if x.startswith("P") or x.startswith("p") else False
print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))

TASK4
numbers = [2, 4, 5, 7, 9, 14]
factor = 2
multiply = [(lambda x: x * factor)(x) for x in numbers]
print(multiply)