# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:22:02 2024

@author: Elyorbek
"""

# in a restourant user input 3 items, and the name of the item with its price
# is shown if it is available. Otherwise, the user is warned there is
# no such items.

foods = {} #foods in a restaurant

foods['soup'] = 20_000
foods['plov'] = 25_000
foods['tea'] =2_000
foods['coffee'] = 5_000
foods['burger'] = 15_000

print("What would you like!\n")
orders =[]

for n in range(3):  #ordering
    order = input(">>>").lower()
    orders.append(order)

print("\n") 
for y_meal in orders: #checking if order is available
    if y_meal in foods.keys():
        print(y_meal, "is", foods[y_meal])

print("\n")
for n_meal in orders: #checking if order is not available
    if n_meal not in foods.keys():
        print("Unfortunately, we don't have", n_meal, "yet!")
        