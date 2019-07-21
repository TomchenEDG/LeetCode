#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List [int]
        :type target: int
        :rtype: List[int]
        """
        dic ={}
        for i in range(len(nums)):
            if target - nums [i] in dic:
                return [dic[target-nums[i]], i]
            dic[nums[i]] = i

def main():
    nums = [2,7,9,11,12,13,14,16,20]
    k = 36
    olb = Solution()
    a = olb.twoSum(nums, k)
    print(a)


if __name__ == '__main__':main()
