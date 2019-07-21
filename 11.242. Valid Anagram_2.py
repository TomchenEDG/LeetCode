#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict ={}
        # 遍历字符串s,构造字典
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        # 遍历字符串t,删除字典
        for c in t:
            s_dict[c] = s_dict.get(c, 0) - 1
        # 遍历字典,查找结果
        for key in s_dict:
            if s_dict[key] != 0:
                return False
        return True


def main():
    s = "anagram"
    t = "nagaram"
    obl = Solution()
    a = obl.isAnagram(s,t)
    print(a)


if __name__ == '__main__':main()
