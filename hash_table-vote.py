# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:26:04 2020

@author: hhyyz
"""

voted={}
def check_voter(name):
    if voted.get(name):
        print("kick him  out")
        
    else:
        voted[name]=True
        print("let him vote")
        
check_voter("lala")
check_voter("eee")
check_voter("lala")
print(voted)