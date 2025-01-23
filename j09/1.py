s1 = {"apple", "banana", "cherry", "apple"}
s2 = {"google", "microsoft", "apple"}

print(s1)
print(s2)

s3 = s1.intersection(s2)
s3 = s1 & s2
s4 = s1 | s2
s4 = s1.union(s2)
s5 = s1 - s2
s5 = s1.difference(s2)
s6 = s1 ^ s2
s6 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)