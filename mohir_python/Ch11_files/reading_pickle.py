# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:42:37 2024

@author: Elyorbek
"""

# reading pickle
import pickle

with open("students_pcl", "rb") as file:
    student_r1 = pickle.load(file)
    student_r2 = pickle.load(file)

print(student_r1)
print(student_r2)