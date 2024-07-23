# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:34:38 2024

@author: Elyorbek
"""

# introduction to OOP
class Student:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
     
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_birth_year(self, cyear):
        return cyear - self.age
    
    def introduce(self):
        return f"I am {self.fname} {self.lname} and {self.age} years old!"
    
def see_methods(item):
        return[method for method in dir(item) if not method.startswith('__')]

student1 = Student('Diyor', "Rakhimov", 19)
student2 = Student('Akrom', "Qobilov", 18)
student3 = Student('Malik', "Saidov", 20)




