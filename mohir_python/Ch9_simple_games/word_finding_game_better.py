# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:14:49 2024

@author: Elyorbek
"""

# word finding game
import random as r
from uzwords import words

# getting random word 
def get_word():
    word = r.choice(words)
    
    while "-" in word or " " in word or "‘"  in word:
        word = r.choice(words)
    
    return word.lower()


# displaying the word
def display(user_letters, word):    
    display_letters = ""
    
    for letter in word:
        if letter in user_letters:
            display_letters += letter
        else:
            display_letters += "-"
    return display_letters


#playing the game
def play():
    word = get_word()
    word_letters = set(word)
    
    user_letters = ""
    print(f"\nI think of a word with {len(word)} letters.\nGuess it !!!\n")
    
    while len(word_letters) > 0:
        # printing the word
        print(display(user_letters, word))
        
        # printing user's all inputs
        if len(user_letters) >0:
            print(f"\nAll letters you entered:\n{user_letters}")
        
        # user input
        letter = input("\n\tEnter a letter: ").lower()
        if letter in user_letters:
            print(f"\nYou have already entered '{letter}'!")
            user_letters += letter
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"\nGood Job! {letter} is true!")
        else:
            print("\nUnfortunately, there is no such a litter in my word!\n")
            
        user_letters += letter
        
    print("\n\tCongratulations!"
          f"you have found '{word}' in", len(user_letters), "chances!")
    
play() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    