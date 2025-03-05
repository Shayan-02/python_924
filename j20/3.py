class Test:
    age = 10


t1 = Test()
try:
    print(t1.age)
except Exception as r:
    print(r)

print("continue")