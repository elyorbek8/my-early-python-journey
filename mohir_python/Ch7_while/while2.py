# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:48:43 2024

@author: Elyorbek
"""

# # while and list
# print("\nLet's make the list of your friends!\n")
# friends = []
# n = 1
# flag = True

# while flag:
#     name = input(f"What is your {n}-friend's name?\n>>>") # adding a name
#     friends.append(name.lower())
#     n+=1
    
#     quest = input("Would you like to add another friend (yes/no)?\n>>>")
#     if quest == 'no':           # checking the availability of another friends
#         print('Your friends are:')
#         for friend in friends:
#             print(friend.title())
#         break


# # while & dictionary

# print("\nLet's make the list of your friends!\n")
# friends = {}
# n = 1
# flag = True

# while flag:
#     name = input(f"What is your {n}-friend's name?\n>>>") # adding a name and age
#     age = input(f'How old is {name.title()}?\n>>>')
#     friends[name.lower()] = age
#     n+=1
    
#     quest = input("Would you like to add another friend (yes/no)?\n>>>")
#     if quest == 'no':           # checking the availability of another friends
#         for name, age in friends.items():
#             print(f'{name.title()} is {age} years old.')
#         break


# while with pop method

students = ["ali", "vali", 'diyor', 'sarvar', 'nosir']
marked_students = {}

while students:
    student = students.pop()
    mark = int(input(f"{student.title()}'s mark is "))
    marked_students[student] = mark
    print(f"{student.title()} has been marked!")
    
    
    






























