# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:14:35 2024

@author: Elyorbek
"""

uns = ['mit', "icl", 'oxford', "harvard", "cambridge", 'stanford',"eth", "nus", "ucl","caltech"]
ranks = list(range(1,11))

for i in range(len(uns)):
    print(uns[i], ':', ranks[i])