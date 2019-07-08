#!/usr/bin/env python 
# -*- coding:utf-8 -*-



def twoSum(numbers: 'List[int]', target: 'int') -> 'List[int]':
    i, j = 0, len(numbers) -1
    while i < j:
        if numbers [i]+ numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        elif numbers [i]+ numbers[j] == target:
            return [i+1, j+1]

numbers = [2,7,11,14]
target = 21

aa = twoSum(numbers, target)
print(aa)