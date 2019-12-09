# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:56:06 2019

@author: smehdi
"""
def string2int(string):
    sum=0
    for i in string:
        sum+=ord(i)
    return(sum)
    

print(string2int("  "))