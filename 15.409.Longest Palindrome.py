#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/12 0012 14:43 
# @Autohor: Sam
# @File   : 409.Longest Palindrome.py

import math
class Solution:
    def longestpalindrome(self, s: str) -> int:
        cnts = {}
        for c in s:
            if c in cnts:
                cnts [c] +=1
            else:
                cnts [c] = 1
        palindrome = 0
        for (key, value) in cnts.items():
            palindrome += math.floor(value /2) *2
        if palindrome < len(s):
            palindrome += 1
        return palindrome