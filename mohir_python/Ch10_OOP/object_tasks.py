# # -*- coding: utf-8 -*-
# """
# Created on Sat Jul 20 15:18:12 2024

# @author: Elyorbek
# """

# # class about cars
# class Car:
#     def __init__(self, company, model, engine, color, price):
#         self.company = company
#         self.model = model
#         self.engine = engine
#         self.color = color
#         self.price = price
#         self.mileage = 0

#     def get_info(self):
#         return f"""Company: {self.company}
# Model: {self.model}
# Engine type: {self.engine}
# Color: {self.color}
# Price: {self.price}
# Mileage: {self.mileage}"""
    
#     def set_mileage(self, mileage):
#         self.mileage = mileage
#         return mileage


# car1 = Car('tesla', 'y', 'electrical', 'grey', 35_000)
# car2 = Car('bmw', 'y', 'hybrid', 'white', 45_000)

# car1.set_mileage(100)
# print(car1.get_info())



# class Telefon:
#     def __init__(self, rangi, model, yili):
#         self.yili = yili

#     def ovoz_kotarish(self,qiymat):
#         self.qiymat



class Parent:
    def __init__(self, name,age):
        self.name = name.lower()
        self.age = 2*age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def parent_method(self):
        print("This is a method from the Parent class.")


class Child(Parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name,age)
        
        
        # Call the constructor of the Parent class

    def greet(self):
        # Override the greet method of the Parent class
        print(f"Hi, I am {self.name} and I am {self.age} years old.")
    def greet(self):
        # Override the greet method of the Parent class
        print("Hi, I'm 3rd and newest greet function")
    def child_method(self):
        print("This is a method from the Child class.")

Child("Elyorbek", 23).greet()


