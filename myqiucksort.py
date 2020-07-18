# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:21:55 2020

@author: hhyyz
"""

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
    return quicksort(less)+[pivot]+quicksort(greater)

print(quicksort([5,10,1,0,76,39,100]))
            