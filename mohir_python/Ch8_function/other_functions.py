# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:14:39 2024

@author: Elyorbek
"""

# # lambda

# surface = lambda a, b: a * b
# print(surface(3,4))

# # lambda in another function

# def power_find(n):
#     return lambda x: x ** n

# square = power_find(2)
# print(square(10))

# cube = power_find(3)
# print(cube(3))


# # map

# from math import sqrt

# nums = list(range(11))

# sqroots = list(map(sqrt, nums))

# print(sqroots)

# def square(x):
#     return x**2

# squares = list(map(square, nums))
# print(squares)


# filtr()

import random as r

nums = r.sample(range(100), 10)

even_nums = list(filter(lambda x: x % 2 ==0, nums))

print(nums)
print(even_nums)














