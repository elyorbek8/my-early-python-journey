# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:51:38 2024

@author: Elyorbek
"""

age = input("Enter your age: ")

try:
    age = int(age)
except ValueError:
    print("You haven't entered integer value!")
else:
    print(f"You were born in {2024 - age}.")
