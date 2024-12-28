lst1 = [1, 2, 3]
lst2 = [[4, "ali", True], 5, 6]

lst1 += lst2
lst1.extend(lst2)

lst3 = lst2.copy()

print(lst2[0][1])