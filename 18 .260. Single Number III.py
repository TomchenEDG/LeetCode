#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/12/29 0029 16:15
# @Autohor: Sam
# @File   : 18 .260. Single Number III.py

class Solution:
    def singleNumber(self, nums):
        diff = 0
        for num in nums:
            diff = diff^num

        mask = diff & (-diff)

        ret = [0, 0]
        for num in nums:
            if (mask & num == 0):
                ret[0] = ret[0]^num
            else:
                ret[1] = ret[1]^num
        return ret





class Solution:
    def singleNumber(self, nums):
        # 把所有的元素进行异或操作，最终得到一个异或值。
        # 因为是不同的两个数字，所以这个值必定不为0；
        diff = 0
        for num in nums:
            diff = diff^num

        # 取异或值，最后一个二进制位为1的数字作为mask，
        # 如果是1，则表示两个数字在这一位上不同。
        mask = diff & (-diff)

        # 通过与这个mask进行与操作，如果为0的分为一个数组，为1的分为另一个数组。
        # 这样就把问题降低成了：“有一个数组每个数字都出现两次，有一个数字只出现了一次，求出该数字”。
        # 对这两个子问题分别进行全异或就可以得到两个解。也就是最终的数组了。
        ret = [0, 0]
        for num in nums:
            # 两个数不相同，放到一组，
            # 相同，则放到另外一组。
            if (mask & num == 0):
                ret[0] = ret[0]^num
            else:
                ret[1] = ret[1]^num
        return ret



def main():
    nums = [1,2,3,1,2,3,4,5]
    r = Solution()
    value = r.singleNumber(nums)
    print(value)



if __name__ == '__main__':main()