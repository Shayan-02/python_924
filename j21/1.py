def sumNumbers(a, b):
    s = a + b
    m = a * b
    yield s
    yield m
    yield a - b

a = sumNumbers(10, 20)
print(next(a))
print(next(a))
print(next(a))
