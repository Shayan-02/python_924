class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        return f"hello I'm {self.name}"
    def sleep(self):
        return f"{self.name} sleep"
    def show_info(self):
        return f"your name is {self.name} and your age is {self.age}"

p1 = Person("reza", 25)
print(p1.sayHello())
print(p1.sleep())
print(p1.show_info())