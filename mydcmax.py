# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:21:09 2020

@author: hhyyz
"""
def DCmax(list):
    if len(list)==2:
        if list[0]>list[1]:
            return list[0]
        else:
            return list[1]
    sub_max=max(list[1:])
    if list[0]>sub_max:
        print('hhhh')
        return list[0]
    else:
        print('jjjjjh')
        return sub_max

    
arr=[100,3,8,9,10,12,15,20,60,90]  
DCmax(arr)
print(DCmax(arr))