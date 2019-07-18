#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 思想：https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
# 二分法，第一种：
# import math
#
# class Solution(object):
#     def mySqrt(self, x: int) -> int:
#         if x <= 1:
#             return x
#
#         l, h = 0, x
#         while l <= h:
#             # math.floor:取下舍
#             # 计算中值m
#             m = math.floor(l + (h - l) / 2)
#             if x / m > m:
#                 l = m + 1
#             elif x / m < m:
#                 h = m - 1
#             elif x / m == m:
#                 return m
#         return h
#
# def main():
#     number = 5
#     obj = Solution()
#     a = obj.mySqrt(number)
#     print(a)
#
#
# if __name__ == '__main__':main()





# # 二分法，第二种：速度快一点！
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         # 为了照顾到 0 把左边界设置为 0
#         left = 0
#         # 为了照顾到 1 把右边界设置为 x // 2 + 1
#         right = x // 2 + 1
#         while left < right:
#             # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
#             # mid = left + (right - left + 1) // 2
#             mid = (left + right + 1) >> 1
#             square = mid * mid
#
#             if square > x:
#                 right = mid - 1
#             else:
#                 left = mid
#         # 因为一定存在，因此无需后处理
#         return left
#
# def main():
#     number = 8
#     obj = Solution()
#     a = obj.mySqrt(number)
#     print(a)
#
#
# if __name__ == '__main__':main()






# 牛顿法：https://leetcode-cn.com/problems/sqrtx/solution/niu-dun-die-dai-fa-by-loafer/

class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')

        if x == 0:
            return 0

        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            # 1e-6 :10的负6次方,0.000001,有的地方使用 epsilon（ϵ）表示 1e-6.
            # 用来抵消浮点运算中因为误差造成的相等无法判断的情况，
            # 它通常是一个非常小的数字，具体多小要根据你的精度需求来设置。
            if abs(cur - pre) < 1e-6:
                return int(cur)

def main():
    number = 8
    obj = Solution()
    a = obj.mySqrt(number)
    print(a)


if __name__ == '__main__':main()