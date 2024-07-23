# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:41:13 2024

@author: Elyorbek
"""
# Incapsulation
from uuid import uuid4

# Car class
class Car:
    """ Car class """
    __num_car = 0
    
    def __init__(self, company, model, engine, color, year, price, mileage=0):
        """ Car class's object's features """
        self.company = company
        self.model = model
        self.engine = engine
        self.color = color
        self.year = year
        self.price = price
        self.__mileage = mileage
        self.__id = uuid4()
        Car.__num_car += 1
    @classmethod
    def get_num_car(cls):
        return cls.__num_car
    
    def get_mileage(self):
        return self.__mileage
    
    def get_id(self):
        return self.__id
    
    # def __str__(self):
    #     return f"Car: {self.company} model {self.model}"
    
    def __repr__(self):
        return f"Car: {self.company} model {self.model}"
    
    def __eq__(self, y):
        return self.price == y.price
    
    def __lt__(self, y):
        return self.price < y.price
    
    def __le__(self,y):
        return self.price <= y.price
    
# Car_dealership class
class Car_dealership:
    """ Car_dealership class """
    def __init__(self, name):
        self.name = name
        self.cars = []
    
    def __repr__(self):
        return f"{self.name} Car Dealership"
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __setitem__(self, i, value):
        self.cars[i]=value
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, *value):
        for car in value:
            if isinstance(car, Car):
                self.cars.append(car)
            else:
                 print("Please, enter cars!")
    
    def __call__(self, *par):
        if par: # checking whether parameters are available
            for car in par:
                self.add_car(car)
        else: # if there is no parameters
                return [car for car in self.cars]
    

car_dealership1 = Car_dealership("Turbo Auto")
print(car_dealership1)   

car1 = Car("Tesla", "Y", "electric", "grey", 2023, 40_000, 100)
car2 = Car("BMW", "x7", "hybrid", "white", 2024, 55_000, 300)
car3 = Car("Chevrolet", "Malibu", "petrol", "grey", 2024, 25_000)
# print(car1)

car_dealership1.add_car(car1, car2)
car_dealership1[1] = Car("Mers", "Mybach", "petrol", "black", 2020, 30_000)















