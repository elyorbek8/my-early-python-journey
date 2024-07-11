# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:54:10 2024

@author: Elyorbek
"""

# uns = ['mit', "icl", 'oxford', "harvard", "cambridge", 'stanford',"eth", "nus", "ucl","caltech"]

# for un in uns:
#     print("do you wont to get in", un, "?")

# nums = list(range(1,11))

# sqrs = []

# for num in nums:
#     sqrs.append(num**2)

# print(nums)
# print(sqrs)

# friends = []
# print("Who are your 5 best friends?")

# for n in range(5):
#     friends.append(input(f"enter your {n+1}-friend's name:"))
# print(friends)
# # print(f"these cods have been repeated {n+1} times")
# print(len(friends))

n = input("How many people have you met today?\n")

people =[]

for order in range(1,int(n)+1):
    people.append(input(f"{order} - person is "))

print(people)
    

