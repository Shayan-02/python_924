lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = list(filter(lambda x: x % 2 == 0, lst))
print(a)

def sums(a, b):
    print(a + b)

sums1 = lambda a, b : a + b

sums(2, 3)
print(sums1(2, 3))

n = [1, 0, 2, 0, 1, 1, 3, 1]
z = ["YES" if i % 2 == 0 else "NO" for i in n]
print(z)