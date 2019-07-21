#!/usr/bin/env python 
# -*- coding:utf-8 -*-




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 首先我们申请一个26位数组
        arr = [0] * 26
        # 遍历字符串s,构造字典
        for c in s:
            arr[ord(c) - ord('a')] += 1
        # 遍历字符串t,删除字典
        for c in t:
            arr[ord(c) - ord('a')] -= 1
        # 遍历字典,查找结果
        for i in arr:
            if i != 0:
                return False
        return True


def main():
    s = "anagram"
    t = "nagaram"
    obl = Solution()
    a = obl.isAnagram(s,t)
    print(a)


if __name__ == '__main__': main()
