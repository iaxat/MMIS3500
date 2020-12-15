# Content Videos


# Class and Objects
# Section 10.1 and 10.2

person = {}
person["name"] = "andy"
person["age"] = 39
person["height"] = 75
person["grades"] = [85, 90, 93]

print("person_dict: ", person)


class Person():
    def __init__(self, name, age, height, grades):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades


p1 = Person("andy", 39, 75, [85, 90, 93])
print(p1)
print(p1.name)
print(p1.age)
print(p1.height)
print(p1.grades)