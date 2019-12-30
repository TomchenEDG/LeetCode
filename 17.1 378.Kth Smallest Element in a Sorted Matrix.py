#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : time
# @Autohor: Sam
# @File   : File


# 二分法，最快的解决该问题
class Solution:
    def kthSmallest(self, matrix, k):
        # 计算小于等于目标值的元素个数，根据递增规则，从右上角开始查找
        def count_num(m, target):
            i = 0
            j = len(m) - 1
            ans = 0
            while i < len(m) and j >= 0:
                if m[i][j] <= target:
                    ans += j + 1
                    i += 1
                else:
                    j -= 1
            return ans

        #  思路：左上角元素最小，右下角元素最大，计算小于等于中间值的元素个数
        left = matrix[0][0]
        right = matrix[-1][-1]
        # 二分法查找
        while left < right:
            mid = (left + right)//2
            # print(' mid = ', mid)
            count = count_num(matrix, mid)
            # print('count = ', count)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left




def main():
    matrix = [[ 1,  5,  9],
              [10, 11, 13],
              [12, 13, 15]]
    k = 8

    run = Solution()
    value = run.kthSmallest(matrix, k)
    print(value)


if __name__ == '__main__':main()
