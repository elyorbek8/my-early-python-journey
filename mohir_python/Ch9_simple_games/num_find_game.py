# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:19:35 2024

@author: Elyorbek
"""

import random as r


# number hiding game. We need to find
def num_find(x=10):
    num = r.randint(1, x) # a random number
        
    print(f"Guess an integer number in the range of 1 and {x}: ")
    hcount = 0
        
    while True:
        hguess = int(input())
        hcount += 1
        if hguess < num:
            print("Guess bigger one!")  
        elif hguess > num:
            print("Guess smaller one!") 
        else:
            print(f"Congratulations!\nYou have found it in {hcount} chances!\n")
            break
        
    return hcount
    

# number finding game. PC needs to find
def num_find_pc(x=10):
    input("It is my turn!\n"
         f"Think a number between 1 and {x}, I will find it!\n"
          "If you have a number, enter any keys."
          " Then, I will guess it!\n>>>")
        
    cguess = r.randint(1, x)
    print("\n",cguess)
            
    down = 1
    up = x
    ccount = 0
                
    while True:
        message = input("\nIf it is bigger than mine, enter '+'\n"
                                "If it is smaller than mine, enter '-'\n"
                                "If it true, enter 't'\n ")
        ccount += 1
                
        if message == '+':
            down = cguess + 1
            cguess = r.randint(down, up)
            print(cguess)
                
        elif message == '-':
            up = cguess - 1
            cguess = r.randint(down,up)
            print(cguess)
                    
        else:
            print(f"Congrats myself!\nI have found it in {ccount} chance!\n")
            break
    return ccount
    
    
# playing the games
def play(x=10):
    offer = True
    while offer:
        hcount = num_find(x)
        ccount = num_find_pc(x)
        print("Overall:")
        
        if hcount < ccount:
            print(f"You have won the game in {hcount} chance!\n "
              f"Mine is {ccount}!")
        elif ccount < hcount:
            print(f"Ha-ha, I have won the game in {ccount} chance!\n"
              f"Yours is {hcount}!")
        else:
            print(f"Draw: {hcount}:{ccount}")

        # finishing the games
        finish = input("\nWould you like to play again (y/n)?\n")
        if finish == 'n':
            offer = False

x= int(input("Enter the range of numbers we can guess in:\n>>>"))
play(x)

























