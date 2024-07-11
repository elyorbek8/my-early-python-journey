# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:44:37 2024

@author: Elyorbek
"""

# 9th July, 2024
# given a number, print the number is divided to the numbers btween 1 and 10.


a = int(input("enter an integer number:\n>>>"))
check =[]

for num in range(2,11):
    if not a % num:
        print(a, "is divided to", num)
        check.append(num)
if len(check ) == 0:
    print(a, "is a prime number!")
        
        
