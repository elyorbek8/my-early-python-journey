# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:41:13 2024

@author: Elyorbek
"""
# Incapsulation
from uuid import uuid4


class Car:
    def __init__(self, company, model, engine, color, year, price, mileage=0):
        self.company = company
        self.model = model
        self.engine = engine
        self.color = color
        self.year = year
        self.price = price
        self.__mileage = mileage
        self.__id = uuid4()
        
    def get_mileage(self):
        return self.__mileage
    
    def get_id(self):
        return self.__id
    
car1 = Car("Tesla", "Y", "electric", "grey", 2023, 40_000, 100)