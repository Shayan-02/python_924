# vorodi nadarad khorooji nadarad
def test1():
    print("hello 1")


# vorodi darad khorooji nadarad
def test2(a):
    print(a)


# vorodi nadarad khorooji darad
def test3():
    return "hello 2"


# vorodi darad khorooji darad
def test4(a):
    return a


# calling
test1()
name = "ali"
test2(name)
print(test3())
print(test4(name), "4")