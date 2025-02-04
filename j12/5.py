from functools import reduce
lst = [22, 13, 5, 7, 13]

mul = 1
for i in lst:
    mul *= i
print(mul)


print(reduce(lambda mamad, shahab: mamad % shahab, lst))
