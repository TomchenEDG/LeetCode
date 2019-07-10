#!/usr/bin/env python 
# -*- coding:utf-8 -*-

nums = [2,0,2,1,1,0,1,2,0,1,0,2]

class Solution:
    def sortColors(self, nums: 'List[int]') -> 'int':
        """
        Do not return anything, modify nums in-place instead.
        """
        head, now, tail = 0, 0, len(nums) -1
        while now <= tail:
            if nums[now] == 0:
                nums[now], nums[head] = nums[head], nums[now]
                now, head = now + 1, head +1
            elif nums[now] == 2:
                nums[now], nums[tail] = nums[tail], nums[now]
                tail -= 1
            else:
                now += 1
        return nums

def main():
    obj = Solution()
    a = obj.sortColors(nums)
    print(a)

if __name__ == '__main__':main()
