# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:18:01 2024

@author: Elyorbek
"""

goods = ['book', 'pen', 'pencil', 'phone', 'pc', 'laptop']

yes_goods =[]
no_goods =[]

print("Welcome to our e-shopping store!")

basket = []

for n in range(1,6):
    good = input(f'Your {n} - item is ')
    basket.append(good.lower())
    
for item in basket:
    if item in goods:
        yes_goods.append(item)
    else:
        no_goods.append(item)


if len(basket) == len(yes_goods):
    print("\nWe have all the items!")
    for al in yes_goods:
        print(al.title())
        
elif yes_goods:
    print("\nWe have these items:")
    for yes in yes_goods:
        print(yes.title())
        
    print("\nUnfortunately, we don't have these items yet:")
    for no in no_goods:
        print(no.title())
else:
    print("\nUnfortunately, We don't have such items yet!")
    for n in no_goods:
        print(n.title())

    
    