# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:09:28 2024

@author: Elyorbek
"""

# word finding game
import random as r
from uzwords import words

# getting random word 

word = r.choice(words)

while "-" in word or " " in word or "‘"  in word:
    word = r.choice(words)
    
print(f"I think of a word with {len(word)} letters.\nGuess it !!!\n")

secrets = []
chances = []
for l in word:
    l = '*'
    secrets.append(l)

print(secrets)

while "*" in secrets:
    # input guess
    chance = input(f"\n\tYour {len(chances) + 1}-chance: ").lower()
    
    # checking if there is the same input
    if chance in chances:
        print(f"\nYou have already entered '{chance}'!")
        
    chances.append(chance)
    
    # checking whether a guess is in the word
    if chance in word:
        # comparing and replacing if true
        print("\nGood Job!")
        for i in range(len(word)):
            if word[i] == chance:
                secrets[i] = word[i]
    else:
        print("\nUnfortunately, there is no such a litter in my word!\n")
        
    print(secrets)
    print(f"\nAll letters you entered:\n{chances}")
print("\n\tCongratulations, you have found it in", len(chances), "chances!")
    

    
    
