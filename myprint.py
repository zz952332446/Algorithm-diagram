# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:13:32 2020

@author: hhyyz
"""

def fun1(i):
    if i>=0:
        fun1(i-1)
        print(i)
        
fun1(4)