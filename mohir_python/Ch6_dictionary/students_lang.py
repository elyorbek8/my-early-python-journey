# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:13:24 2024

@author: Elyorbek
"""

students = {'ali':['english','uzbek'], 'vali':["english", 'russian','uzbek'],
            'tom':['english','german']}

for name, lans in students.items():
    print(f'\n{name.title()} can speak in some languages:', end=" ")
    for lan in lans:
        print(f'{lan.title()}', end=" ")

    