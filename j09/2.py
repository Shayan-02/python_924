def salam1():
    print("salam1")


def salam2():
    return "salam2"


a = salam1()
print(salam2()*2)

def salam3(name, age):
    print("salam", name, "you are", age, "years old")


salam3("ali", 20)
salam3("reza", 25)
salam3("saeed", 33)

def salam4(name, age):
    return "salam", name, "you are", age, "years old"


print(salam4("mohammad", 30))