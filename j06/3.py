ali = 1, 2, 3
print(ali) # (1, 2, 3)
print(type(ali)) # <class 'tuple'>

b = list(ali)
b[2] = "reza"
ali = tuple(b)
print(ali) # (1, 2, 4)
