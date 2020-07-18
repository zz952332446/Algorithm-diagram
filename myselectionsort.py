# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:17:40 2020

@author: hhyyz
"""

def findsmallest(arr):
    smallest=arr[0]
    smallest_index=0  ###重要
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
            
    return smallest_index
        


def selectionsort(arr):
    new=[]
    for i in range(len(arr)):
        smallest=findsmallest(arr)
        new.append(arr.pop(smallest)) #pop内传递的是index
    return new

print(selectionsort([3,2,10,44,2,57,13]))