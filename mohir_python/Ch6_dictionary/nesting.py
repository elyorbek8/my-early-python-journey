# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:09:07 2024

@author: Elyorbek
"""

car0 ={"model":"nexia", "price":5000, "color":"blue", 'year': 2008}
car1 ={"model":"captiva", "price":15000, "color":"black", 'year': 2019}
car2 ={"model":"malibu", "price":25000, "color":"grey", 'year': 2024}

cars = [car0, car1, car2]

for car in cars:
    print(f"model: {car['model']}, "
          f"price: {car['price']}, "
          f"color: {car['color']}, "
          f"year: {car['year']}. ")


    