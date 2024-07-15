# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:36:19 2024

@author: Elyorbek
"""
# # using *arg 
# def sum_finder(*nums):
#     summ = 0
#     for num in nums:
#         summ += num
#     return summ

# print(sum_finder(1,2,3,4))

# using **kwarg
def car_info(company, model, **info):
    """ the function that shows info about a car in a list """
    info['company'] = company
    info['model'] = model
    
    return info

car1 = car_info('tesla', 'x', color = 'blue', engine = 'electric')
car2 = car_info('bmw', 'i5', max_speed = 250, colour = 'white')