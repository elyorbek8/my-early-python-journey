# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:26:02 2024

@author: Elyorbek
"""
# the function that shows full name
def get_name(fname, lname, mname=''):
    if mname:
        return f"{fname} {lname} {mname}".title()
    else:
        return f"{fname} {lname}".title()    
    
print(get_name("diyor", "aliyev", "valijon ugli"))

