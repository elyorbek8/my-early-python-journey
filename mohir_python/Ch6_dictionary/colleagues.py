# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:33:57 2024

@author: Elyorbek
"""
# nesting: the dictionary in a dictionary;
# list in the  dictionary 

colleagues = {'eldor':{'surname':'gafforov', 'age':18,
                       'languages':['english', 'russian', 'uzbek']},
              'abdulaziz':{'surname':'akhmatov', 'age':19,
                       'languages':['uzbek', 'german', 'english']},
              'bobur':{'surname':'alimov', 'age': 19,
                       'languages':['english', 'uzbek', 'arabic']}}

for name, info in colleagues.items():
    print(f'\n\n{name.title()} {info["surname"].title()}:\n'
          f'Age: {info["age"]}\n'
          f'He knows the following languages:', end=" ")
    for lan in info['languages']:
        print(lan.title(), end=" ")