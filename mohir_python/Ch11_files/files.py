# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:21:10 2024

@author: Elyorbek
"""

# working with files

# simple but not prefered way
# file = open("pi.txt")
# PI = file.read()
# print(PI)
# file.close()

# prefered way
# with open("pi.txt") as file:
#     PI = file.read()

# print(PI)
# PI = float(PI)

# filename = "student_data/students.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     students = file.readlines()

# print(students)

# students = [student.rstrip().lower() for student in students]
# print(students)

# writing into file: "w" mode
filename = 'new_file.txt'
# name = 'Asibekov Davron'
# age = 19

# with open(filename, "w") as file:
#     file.write(name + "\n")
#     file.write(str(age) + "\n")

# writing into file: "a" mode
with open(filename, "a") as file:
    file.write("Alibekov Kamol\n")
    file.write("20")

