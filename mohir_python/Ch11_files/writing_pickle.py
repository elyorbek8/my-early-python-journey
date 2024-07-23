# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:27:54 2024

@author: Elyorbek
"""

# working with pickle module
# writing
import pickle

student1 = {"first name":"alisher", "last name":"botirov", "age":21}
student2 = {"first name":"sardor", "last name":"rashidov", "age":20}

with open('students_pcl','wb') as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)
