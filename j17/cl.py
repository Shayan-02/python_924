class Person:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def sleep(self):
        return f"{self.name} sleep"

    def _work(self):
        return f"{self.name} work"

    def __show_info(self):
        return f"your name is {self.name} and your age is {self.age}"
