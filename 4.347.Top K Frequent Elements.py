#!/usr/bin/env python 
# -*- coding:utf-8 -*-


nums = [1,1,1,2,2,3]
k = 2

class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int')-> 'List[int]':
        frequent_of_number ={}
        for num in nums:
            frequent_of_number[num] = frequent_of_number.get(num, 0) + 1
        # 建桶
        buckets = [[] for i in range(len(nums) + 1)] # 如果用 []*(len(nums )+1) 则是浅拷贝
        for key, value in frequent_of_number.items ():
            buckets[value].append(key)

        result =[]
        for x in range(len(nums), -1,-1):
            if k > 0 and buckets[x]:
                result += buckets[x]
                k -= len(buckets[x])
            if k == 0:
                return result

def main():
    obj = Solution()
    a = obj.topKFrequent(nums, k)
    print(a)

if __name__ == '__main__':main()
