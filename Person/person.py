# class Mammal:
#     def breathe(self):
#         return "inhale and exhale"
#
#
# class Cat(Mammal):
#     def speak(self):
#         return "Meow"
#
#
# rani = Cat()
# print(rani.breathe())


class Person:
    """Person Class"""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hi, my name is {}".format(self.name)


class Student(Person):
    """Student Class"""

    def learn(self):
        return "I get it!"


class Instructor(Person):
    """Instructor Class"""

    def teach(self):
        return "An object is an instance of a Class!"


Nadia = Instructor("Nadia")
print(Nadia.greet())
print(Nadia.teach())
Daniel = Student("Daniel")
print(Daniel.greet())
print(Daniel.learn())
