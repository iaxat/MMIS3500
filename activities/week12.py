# Content Videos
import numpy as np

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

    def calc_avg_grades(self):
        return np.mean(self.grades)


    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.height

    def get_height(self):
        return self.height

    def get_grades(self):
        return self.grades
    

    def set_name(self,name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def set_height(self,height):
        self.height = height
    
    def set_grades(self, grades):
        self.grades = grades

p1 = Person("andy", 39, 75, [85, 90, 93])
print(p1)
print(p1.name)
print(p1.age)
print(p1.height)
print(p1.grades)
print(p1.calc_avg_grades())


#  Section 10.3
# Continuation of Classes and Objects

