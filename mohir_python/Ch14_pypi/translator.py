# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:56:28 2024

@author: Elyorbek
"""

# Gtranslator
from googletrans import Translator

tr = Translator() # translator obj

text_uz = input("Tarjima qilmoqchi bo'lgan matnni kiriting:\n")

tr_text = tr.translate(text_uz, dest='en')

print(tr_text.origin) # original text

print(tr_text.text) # translated text

print(tr_text.src) # showing the source of original text

