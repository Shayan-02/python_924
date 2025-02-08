import numpy as np
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sums = 0
l = 0
for i in lst:
    sums += i
    l += 1

print(sums/l)

print(sum(lst)/len(lst))

ar = np.array(lst)
print(ar.mean())

arr = np.arange(1, 1001, 5)
print(arr)
print(arr.max())