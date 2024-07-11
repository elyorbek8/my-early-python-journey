# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:45:55 2024

@author: Elyorbek
"""

malibus = []

for n in range(11):
    new_car = {"model":"malibu",
               "color":None,
               "controller":None,
               "price":None}
    malibus.append(new_car)
    
    
for car in malibus[:5]:
    car['color'] = 'black'
    car['controller'] = 'avto'
    
for car in malibus[5:8]:
    car['color'] = 'white'
    car['controller'] = 'mechanic'

for car in malibus[8:]:
    car['color'] = 'grey'
    car['controller'] = 'avto'
    
for car in malibus:
    if car['controller'] == 'avto':
        car['price'] = 40_000
    else:
        car['price'] = 35_000
        

for malibu in malibus:
    print(f"model: {malibu['model']}\n"
          f"color: {malibu['color']}\n"
          f"controller type: {malibu['controller']}\n"
          f"price: {malibu['price']}\n")




















