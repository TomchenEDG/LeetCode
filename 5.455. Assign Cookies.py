#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Solution:
    def findContentChildren(self, appetite, biscuit):
        appetite = sorted(appetite)
        biscuit = sorted(biscuit)
        cnt_appetite = 0
        cnt_biscuit = 0
        while cnt_appetite < len(appetite) and cnt_biscuit < len(biscuit):
            # 饼干大于等于人的胃口,满足人的胃口,人数加一
            if appetite[cnt_appetite] <= biscuit[cnt_biscuit]:
                cnt_appetite += 1
            # 不管满不满足,饼干都耗费了一个
            cnt_biscuit +=1
        return cnt_appetite

def main():
    nums = [3, 2, 4]
    s = [4, 3, 1]
    obj = Solution()
    a = obj.findContentChildren(nums, s)
    print(a)

if __name__=="__main__":main()


# nums = [2, 3, 5, 4, 4, 3]
# s = [1, 1, 2, 3, 5, 2, 4 ,2 ,3]
#
# list_a = []
# for s in s:
#     for n in nums:
#         if s == n:
#             list_a.append(s)
#
# print(len(set(list_a)))