lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst2 = []
for i in lst:
    lst2.append(i**2)

print(lst2)

lst3 = [i**2 for i in lst if i % 2 == 0]
print(lst3)