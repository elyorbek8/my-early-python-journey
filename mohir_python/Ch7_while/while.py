# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:26:56 2024

@author: Elyorbek
"""
# # a simple while example
# num = 1

# while num <= 10:
#     print(num)
#     num = num +1


# # while with input

# quest = ("enter a number!")
# quest += "If you want to stop, enter 'exit'!\n>>>"

# box = " "

# while box != 'exit':
#     box = input(quest)
#     if box != 'exit':
#         print(float(box)**2)
# print("the program has ended!")



# # while with a flag

# quest = ("enter a number!")
# quest += "If you want to stop, enter 'exit'!\n>>>"

# box = " "
# flag = True

# while flag != False:
#     box = input(quest)
#     if box != 'exit':
#         print(float(box)**2)
#     else:
#         flag = False
# print("the program has ended!")
    

# break in while

# quest = ("enter a number!")
# quest += "If you want to stop, enter 'exit'!\n>>>"

# box = " "

# while True: # forever cycle
#     box = input(quest)
#     if box == 'exit':
#         break # stopping the cycle
#     else:
#         print(float(box)**2)
# print("the program has ended!")

# # continue in for operator

# for num in range(1,10):
#     if num == 3:
#         continue
#     print(f'square of {num} is {num**2}.')


# # museum ticket price by age range

n = 1

while True:
    age = int(input(f"How old is {n}-visitor?\n>>>"))
    
    if age <= 7: # checking ticket price
        price = 0
    elif age > 7 and age <=18:
        price = 3_000
    elif age > 18 and age < 65:
        price = 7_000
    else:
        price = 0
   
    if price == 0: # showing a particular ticket price
        print('ticket is free\n')
        n= n+1
    else:
        print(f'ticket price is {price} sum\n')
        n+=1
    
    quest = input("Would you like to buy ticket again (yes/no)?\n>>>")
    if quest == "no":
        print("have a great time!")
        break
      