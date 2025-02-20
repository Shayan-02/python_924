class Alive:
    def move(self):
        pass


class Fish(Alive):
    def move(self, name):
        return f"{name} is swimming"


class Snake(Alive):
    def move(self, name):
        return f"{name} is a snake and crowling"


f1 = Fish()
print(f1.move("bob"))

s1 = Snake()
print(s1.move("jerry"))