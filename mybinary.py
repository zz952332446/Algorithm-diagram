# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:02:29 2020

@author: hhyyz
"""

def binary_search(arr,item):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=int((low+high)/2)
        guess=arr[mid]
        if guess<item:
            low=mid+1
        if guess>item:
            high=mid-1
        if guess==item:
            return mid
        else:
           return 0
        
array=[2,6,9,10,15,18,100]
print(binary_search(array,15))
                