s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s3 = s1.intersection(s2)
# s1.intersection_update(s2)

s4 = s1.difference(s2)
# s1.difference_update(s2)

s5 = s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)

s6 = s1.union(s2)
# s1.update(s2)