class Person:
    def __init__(self, name, job, age=0):
        self.name = name
        self.age = age
        self.job = job


    def eating(self):
        return f"{self.name} is eating..."

    def sleep(self):
        return f"{self.name} is sleep"
    
    def show_info(self):
        return f"{self.name} is {self.age} years old.\n{self.name} is a {self.job}"


class Student(Person):
    def __init__(self, name, job, major, grade):
        super().__init__(name, job=None)


s1 = Student("ali", 20, "computer student")
print(s1.show_info())
