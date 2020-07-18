# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:40:07 2020

@author: hhyyz
"""

def bubble_sort(nums):
    for i in range(len(nums)-1):  # 这个循环负责设置冒泡排序进行的次数,最后一次不需要
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
 
print(bubble_sort([45, 32, 8, 33, 122, 22, 19, 97]))