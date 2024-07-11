# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:06:48 2024

@author: Elyorbek
"""

meals = ["soup", 'beef', 'plov', 'burger','tea']
orders = ['coffee', 'plov', "tea", 'burger', 'coda']

if orders:
    for meal in orders:
        if meal in meals:
            print(f"Yes, we have {meal}.\n Please, wait a minute!")
        else:
            print(f"Unfortunately, right now we don't have {meal}.\n Would you like something else!")
else:
    print("We haven't any orders yet!")