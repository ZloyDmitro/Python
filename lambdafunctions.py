add1 = lambda x: x + 2
print(add1(2))
def add1(x): 
    return x + 2
print(add1(4))

mult1 = lambda y: y*2
print(mult1(2))
print(add1(2)*mult1(2))
print(add1(2)**mult1(2))

mufunc = lambda x, y: x ** y
result = mufunc(3, 6)
print(result)
def myFunc2(x, y):
    return x**y
result = myFunc2(2,3)
print(result)