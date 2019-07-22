#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# lambda函数实现快速排序
quick_sort = lambda array: \
    array if len(array) <= 1 \
        else quick_sort([item for item in array[1:] if item <= array[0]]) + \
             [array[0]] + \
             quick_sort([item for item in array[1:] if item > array[0]])

# 正常实现快速排序
def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)

nums = [2, 3, 1, 4]
a = quick_sort(nums)
print(a)