#!/usr/bin/env python 
# -*- coding:utf-8 -*-



# from sklearn.tree import DecisionTreeClassifier
# import numpy as np
#
#
# X = np.array([[0, 0,  1],
#               [0, 1,  0],
#               [1, 0,  0],
#               [1, 1,  0]])
# y = np.array([0, 0, 0, 1])
#
# t = np.array([[0, 0,  1],
#               [0, 1,  0],
#               [1, 0,  0],
#               [1, 1,  0]])
#
# clf = DecisionTreeClassifier()
#
# clf.fit(X, y)
# print(clf.predict(t))

# PCA
# import numpy as np
# from sklearn.decomposition import PCA
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# pca = PCA(n_components=2)
# pca.fit(X)
# print(pca.explained_variance_ratio_)
# print(pca.singular_values_)


# import numpy as np
#
# a = np.arange(1,3).reshape(2,1)
# print("a:",a)
# b = np.arange(1,3).reshape(1,2)
# print("b:",b)
# print(np.dot(a.T,b.T))


# import numpy as np
#
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
#
# print(np.vstack((arr1, arr2)))
# print(np.hstack((arr1, arr2)))

# 正负无穷大
# x = float('inf')
# print(x)

# 字符转换为十进制
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))

# 递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
#
# a = fact(3)
# print(a)

# np.argsort(X) 从小到大的索引值
# import numpy as np
# X = np.array([1,3,2,4,4,2])
# print(X)
# sorted_index = np.argsort(X)
# print(sorted_index)

# # not
# list_numbers = [1,2,3]
# if not list_numbers:
#     print("False")
#
# bool()
# list_numbers = [1]
# print(bool(list_numbers))
#
# all()函数：用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，
# 如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。
# print(all(n<4 for n in list_numbers))

# 是否逐个打印字符？会的
# input = '2-1-1'
# for c in input:
#     print(c)

# None ：判断是否等于None
# class Foo(object):
#     def __eq__(self, other):
#         return None
#
# foo = Foo()
# print(foo)
# print(foo==None) # 这种是错的
# print(foo is None) # 正确的做法

# continue
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       continue
#    print('当前字母 :', letter)

# arr all()可以用到列表里面都为0
# arr = [0] * 26
# print(arr)
# if not all(arr):
#    print("完成")

# arr 打印：True
# arr = {'a':0,'b':0}
# print(all(arr))

# 看字典长度？ 可以，等于2
# arr = {'a':0,'b':0}
# print(len(arr))

# 单个只能循环value
# arr = {'a':0,'b':0}
# for value in arr:
#    print(value)

# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# print('a'.join('1234'))
# print('a'.join('bcde'))

# .center .ljust .rjust .zfill
# name= 'albert'
# print(name.center(30,'-'))
# print(name.ljust(30, '*'))
# print(name.rjust(30,'*'))
# print(name.zfill(50)) #用0填充

# Python expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# name='albert\thello'
# print(name)
# print(name.expandtabs(1))

# # captalize(), swapcase(), title()
# name='albert\thello'
# print(name)
# print (name.capitalize()) # 首字母大写
# print(name.swapcase ()) # 大小写翻转
# msg = 'albert say hi'
# print(msg.title()) # 每个单词的首字母大写

print(num4.isnumeric()) # True



