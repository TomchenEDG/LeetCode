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

# .isnumeric() isnumberic:unicode,中文数字,罗马数字
# num1 = '一' # 中文数字
# num2 = '1' # 阿拉伯数字
# num3 = 'Ⅰ' # 罗马数字
# print(num1.isnumeric())
# print(num2.isnumeric())
# print(num3.isnumeric())

# Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
# num1 = '12df'
# num2 = '12'
# num3 = '二'
# print(num1.isdecimal())
# print(num2.isdecimal())
# print(num3.isdecimal())

# Python isdigit() 方法检测字符串是否只由数字组成。
# num1 = '12df'
# num2 = '12'
# num3 = '二'
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())

# name = 'alb123ert'
# print(name.isalnum()) # 字符串由字母 或 数字组成
# print(name.isalpha()) # 字符串只由字母组成
# print(name.isidentifier()) # 用于判断字符串是否是有效的Python 标识符
# print(name.islower()) # 检测字符串是否由小写字母组成。
# print(name.isupper()) # 检测字符串中所有的字母是否都为大写。
# print(name.isspace()) # 检测字符串是否只由空格组成。
# print(name.istitle()) # 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。

# .extend 逐个增加元素
# l1 = [1, 2, 3, 4, 5, ]
# l1.append ([6, 7, 8, 9, ])
# print("append:\n", l1)
#
# l1.extend([6, 7, 8, 9])
# print("extend:\n", l1)

# .extend()
# l1= [1, 2, 3, 4, 5, ]
# l1.extend([6, 7, 8, 9])
# print (l1)
#
# l1.extend('abc')
# print(l1)
#
# l1.extend('a') #也是可迭代对象
# print(l1)
#
# # l1.extend(1) #报错,不可选代，使用.extend()必须是可迭代对象。1 不是。
# print(l1)

# .clear() 清除里面的元素，返回空列表
# l1 = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
# l1.clear()
# print (l1)


# .index()
# l1 = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
# print(l1.index('b',1, 4)) # 两个数字分别对应 起始位置 和 结束位置


# 切片
# l1 = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
#
# print(l1[:-1]) # 除了最后一个，其他全部显示
# print(l1[:-2]) # 除了最后两个，其他全部显示
# print(l1[5:1:-2]) # 从索引5 到 索引1 ，每隔两个数打印出来


# 统计
# print(['a', 'b', 'c', 'd', 'e', 'b', 'c', 'a', 'a'].count ('a'))


# 反序排序
# l1 = ['a', 1, 'b', 'c', 'd', 'e', 'b', 'c']
# l1.reverse()
# print(l1)



# sort按照ascii码来进行排序
# l1 = ['a', '1', 'b', 'c', 'd', 'e', 'b', 'A', 'Z', 'c']
# print(l1)
#
# l1.sort()
# print(l1)
#
# l1.sort(reverse=True)
# print(l1)



# 关于内存
# list1 = [1, 2, [3, 4], [5, [6, 7]]]
# print('list1:', id(list1))
# print ([id(i) for i in list1])
#
# list2 = list1
# print('list2:', id(list2))
# print ([id(i) for i in list2])
#
# print(list1[0] is list2[0])
# print(list1[2] is list2[2])
#
# list2[0] = -1 # 更改list2也会改变list1的值，因为他们指向同一个id
# print(list1)
#
# list2[2][1] = -1
# print(list1)




# 理解浅拷贝
# from copy import copy
# list1= [1, 2, [3, 4], [5, [6, 7]]]
# print('list1:', id(list1))
# print([id(i) for i in list1])
#
# list2 = copy(list1)
# print('list2:', id(list2))
# print([id(i) for i in list2])
#
# # 1 判断论证过程
# print(list1 is list2) # id不同自然不是, id用来形象表示内存地址
# print(list1[0] is list2[0]) # 两者之间对应的元素都指向同一个地址
# print(list1 [2] is list2[2])
#
# # 2 对一级元素整体修改论证 ( 其实 此时 可变类型元素 也只能当作不可变来修改 )
# list1[0] = -1 # 修改列表 1 或 2 都是单独变化的
# print(list1)
# print(list2)
#
# list2[1] = -2
# print (list1)
# print (list2)
#
# list1[2] = -3
# print (list1)
# print(list2)
#
# list2[2] = -30
# print(list1)
# print(list2)
#
# # 3 给对象添加元素
# list1.append ('addl')
# print(list1)
# print(list2)
#
# list2.append ('add2')
# print(list1)
# print(list2)
#
# # 4 删除
# list1.pop()
# print(list1)
# print(list2)
#
# list2.pop()
# print(list1)
# print(list2)
#
# # list1.pop()
# # print (list1)
# # print (list2)
#
# # 5 只有对 对象 内一个 可变类型元素内的 元素的修改(包含添加,修改和删除) ,才会同步
# # list2[-1][0] = '5->55'
# # print (list1)
# # print(list2)
#
# # 换成list1也是一样,但需要把上面的部分代码注释掉,确保索引位置不会出错
# list1[3][0] = '5->550 '
# print('list1:',list1)
# print('list2:',list2)





# 理解深拷贝
# import copy
# list1 = [1, 2, 3, 4, 5, [6, 7, 8, ]]
# list2 = copy.deepcopy(list1)
# print(id(list1))
# print(id(list2))
#
# list1[5].append(9)
# print(list1)
# print(list2)
#
# list1.append(6)
# print(list1)
# print(list2)
#
# list1.pop()
# print(list1)
# print(list2)



# 元组，不可更改,只可取值
# age = (12,3,4)
# age[0] = 1
# print(age[0])



# 字典 .fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
# l1={'name':'albert', 'age':18, 'gender': 'male'}
# # 第一个参数：迭代循环的字典的key；
# # 第二个参数：表示value,可以多个key循环对应这个value,也可以只有一个key,也可以没有value；
# a = l1.fromkeys(l1, 'I am Albert')
# print(a)
#
# b = dict.fromkeys('name') # 必须有一个可迭代类型,作为字典的key
# print (b)
#
# b = dict.fromkeys('e') # 也可以迭代
# print(b)
#
# b = dict.fromkeys ( [1,2,3,])
# print(b)




# 删除字典 del
# l1= {'name': "albert",'age': 18, 'gender':'male'}
# del l1['name']
# print(l1)




# 删除字典键，pop()
# l1= {'name': 'albert','age': 18,'gender': 'male'}
# res = l1.pop ('name') # 删除指定key的value,并拿到一个返回值
# print(res)
# print(l1)



# 删除字典键，.popitem()
# l1= {'name':'albert', 'age':18, 'gender':'male'}
# res2 = l1.popitem() # 随机返回 并 删除字典中的一对键和值(一般删除末尾对)。
# # 如果字典已经为空,却调用了此方法,就报出KeyError异常。
# print(res2)
# print(l1)



# setdefault()，只添加不修改
# d1={'name':'albertage', 'age':18,}
# d1.setdefault('name','Albert')
# d1.setdefault('gender','male')
# print(d1)




# update(),既添加也修改
# d1={'name':'albertage','age': 18}
# d1.update({'name':'Albert', 'gender':'male'}) # 注意传参方式的不同
# print(d1)



# enumerate()，枚举，打印 key的索引 和 key
# d1 = {'name':'albertage','age': 18}
# for a in enumerate(d1):
#    print(a)



# 一次性获取字典所有key，value
# d1={'name':'albertage','age': 18}
# # a = d1.keys()
# # print(list(a))
# #
# # b = d1.values()
# # print(list(b))
# #
# # c = d1.items()
# # print(list(c))



# collections容器数据类型

# namedtuple(),命名元组
# from collections import namedtuple # 从collections库中导入namedtuple (导入外部)
# # 创建一个命名元组对象
# point = namedtuple('p', ['x', 'y']) # p代表名称, "x"和"y"为内容
# p = point(1, 2)
# print(p)
# print(p.x) #1
# print(p.y) #2




# 类似列表(list)的容器, 实现了在两端快速添加(append)和弹出(pop)
# from collections import deque
#
# d = deque('abcd')
# for i in d:
#    print(i)
# print('d[0]:',d[0])
# print('d[1]:',d[1])
#
# d.append('e') # 从右边加入
# print('右边加入e:',d)
#
# d.appendleft('x') # 从左边加入
# print('左边加入x:',d)
#
# d.pop() # 从右侧弹出
# print('右边删除e:',d)
#
# d.popleft() # 从左侧弹出
# print('左边删除x:',d)
#
# deque(reversed(d)) #反转顺序
# print(d)
# #d = list(d) #转化成1ist
# #d = list(reversed(d))
# #print(d)
# d.extend('xyz') # 从右侧添加
# print('从右侧添加xyz:',d)
#
# d.extendleft('nba') # 从左侧添加
# print('从左侧添加nba:',d)
#
# d.rotate(1) # 把最右边的元素挪到最左边
# print('把最右边的元素挪到最左边:',d)
#
# d.rotate(-1) # 把最左边的元素挪到最右边
# print('把最左边的元素挪到最右边:',d)
#
# d.clear() #清空
# d.pop()  #报错



# ChainMap 链映射
# from collections import ChainMap
# # 链映射的用法
# dict1 = {'name':'Albert', 'age':18}
# dict2 = {'weight':65, 'height':180}
# res = list(ChainMap(dict1, dict2))
# print(res)



# 判断字典.keys()是否包含所有关键值
# dict1 = {'name':'Albert', 'age':18}
# print('name'in dict1.keys())



# 获取当前这个feature.py的地址
# import sys
# list_test = sys.argv
# print(list_test)


# pop()
# list_a = [1,2,3]
# list_b = list_a.pop()
# print(list_b)
# print(list_a)



# 查找字符 X.index()
# info = 'abca'
# print(info.index('a'))
# print(info.index('b'))
# print(info.index('c'))
# print(info.index('a'))



# capitalize():首字母大写
# info = 'abca,bdbd'
# print(info.capitalize())



# title():每个单词的首字母大写
# info = 'abca,bdbd'
# print(info.title())



# swapcase():大小写反转
# info = 'abca,bdbd'
# print(info.swapcase())



# isidentifier() 用于判断字符串是否是有效的 Python 标识符，
# 可用来判断变量名是否合法。
# print( "if".isidentifier() )
# print( "def".isidentifier() )
# print( "class".isidentifier() )
# print( "_a".isidentifier() )
# print( "中国123a".isidentifier() )
# print( "123".isidentifier() )
# print( "3a".isidentifier() )
# print( "".isidentifier() )

# .fromkeys():建立字典
# b = dict.fromkeys([1,2,3],["a",'b','c'])
# print(b)
# b = dict.fromkeys('e')
# print(b)


# del 字典删除
# b = dict.fromkeys([1,2,3],["a",'b','c'])
# print(b)
# del b[1]
# print(b)


# pop 字典删除
# b = dict.fromkeys(['name',2,3],["a",'b','c'])
# print(b)
# b.pop('name')
# print(b)


# .setdefault():只添加不修改
# d1 = {'name':'albert',
#       'age':18,
# }
# d1.setdefault('name','Albert')
# d1.setdefault('gender','male')
# print(d1)

# update():既添加也修改
# d1 = {'name':'albert',
#       'age':18,
# }
# d1.update({'name':'Albert', 'gender':'male'})
# print(d1)

# 枚举:(0, 'name') (1, 'age')
# d1 = {'name':'albert',
#       'age':18,
# }
# for a in enumerate(d1):
#     print(a)


# range():怎么打印的？不会打印10，顾头不顾尾
# for i in range(1,10):
#     print(i)


# a 不是 b，所以true
# a = 1
# b = 2
# if  a is not b:
#     print('12')



# 三种函数返回None
# def foo():
#     pass
# def foo1():
#     return
# def foo2():
#     return None
# re,re1,re2 = foo(),foo1(),foo2()
# print(re,re1,re2)



# 返回不同组合的数据，返回后变成元组
# def func():
#     return 1,2,3,[1,2,3]
# re=func()
# print(re)



# 默认参数
# m = 10
# def func(i,y=m):
#     print(y, i)
# func(1)



# 可变长参数 *args
# def func(x,y,*args):
#     print(x,y,args)
# func(1,2, 3,4,5,6,7,8)



# 可变长参数 **args
# def func(x,y,**kwargs):
#     print(x,y,kwargs)
# func(x=1,y=2,z=3,a=1,b=2,c=3)



# 使用各种实参来测试*args
# def foo(x,y,z,*args):
#     print(x,y,z)
#     print(args)
# foo(1,2,3,*[1,2,3,4,5,6])
# foo(1,2,3,*(1,2,3,4,5,6))
# foo(1,2,3,*'hello')
# foo(1,2,3,*{'a':1,'b':2})
# foo(*[1,2,3,4])



# 需注意的点：
# def foo(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# foo(*[4,5,1])
# foo(*[4,5])


# 溢出的参数都为放到了 kwargs
# def auth(name,password,**kwargs):
#     print(name)
#     print(password)
#     print(kwargs)
#
# # auth(name='Albert',password='123')
# auth(name='Albert',password='123',group='group1',groups='group2')



# 组合使用:*args **kwargs
# def index(name, age, gender):
#     print('welcome %s %s %s'%(name, age, gender))
#
# def wrapper(*args, **kwargs):
#     print("args:",args)
#     print("kwargs:",kwargs)
#     index(*args, **kwargs)

# wrapper(name='Albert', age=18, gender='male')
# wrapper('Albert', age=18, gender='male')
# wrapper('Albert', 18, gender='male')
# wrapper(18,'Albert',  'male')



# 使用命名关键字参数
# def foo(x, y, *, z):
#     print(x, y, z)
# # foo(1,2)
# # foo(1,2,3)
# # foo(1,2,a=3)
# foo(1,2,z=3)



# 熟练*args
# def auth(*args, name, pwd):
#     print(name, pwd)
# auth(pwd='123', name='Albert')


# pop()
# a = [1,2,3,4,5]
# for i in range(0,len(a),2):
#     a[i] = 0
# for i in a:
#     if not i:
#         a.remove(i)
# print(a)



# 元组
# a = (1,1)
# b = (2,2)
# c = a + b
# print((c[0],))

# 列表
# a = [12,3]
# b = [1,1]
# c = a+b
# print(c)



# pop()删除里面的最后一个{}
# c = 1
# def add():
#     print(c)
# def addd():
#     print(c)
# add()
# addd()



# 列表里面放字典
# a = [{1},{}]
# print(a)
# a.pop()
# print(a)



# 切片回忆
# a ='abcd123'
# print(a[:2])



# 倒转打印列表的值
# a = [1,2,3,4]
# for i in range(len(a),-1,-1):
#     print(i)


# 可变长参数
# def aa(x,y,*args):
#     return x,y,args
#
# b = aa(1,2,3,4,5,6)
# print(b)



# 实参添加 * 等于打散实参值
# def aa(x,y,z,*kwargs):
#     return x,y,z,kwargs
# # b = aa(x=1,y=2,z=3,a=1,b=2,c=3)
# # print(b)
# # b = aa(1,2,3,*(4,5,6,7,7))
# b = aa(1,2,3,'hello','world')
# print(b)



# * 使用来打散实参
# def foo(x,y,z):
#     print(x,y,z)
#
# foo(*'hel')



# ** 也是打散值
# def foo(x,y,z):
#     print(x,y,z)
#
# foo(1,**{'z':2,'y':3})


# 限制关键字名称
# def auth(*args, **kwargs):
#     if len(args)!=0:
#         print('必须用关键字的形式传参')
#         return
#     if 'name' not in kwargs:
#         print('必须用指定的key名name')
#         return
#     if 'pwd' not in kwargs:
#         print('必须用指定的key名pwd')
#         return
#
#     name = kwargs['name']
#     pwd = kwargs['pwd']
#     print(name, pwd)
#
# auth(x='Albert', y='123')
# auth('Albert', '123')
# auth('Albert', pwd='123')
# auth(name='Albert', pwd='123')


# * 后面都限制为关键字参数
# def auth(*args, name, pwd):
#     print(name, pwd)
#
# # auth(name='Albert', pwd='123')
# auth('Albert', '123')


# math.floor：向下取
# import math
# a = math.floor(1)
# print(a)



# 字典
# menu = {'汽车':
#             {'轿车':
#                  {'宝马':
#                       {'宝马760'}}}}
#
# layers = [menu, ]
#
# print(layers[-1])
#
# for key in layers:
#     print(key)

# 字符搜索
# s = 'jr_shenjing'
# if 'shenjing' in s:
#     print(True)



# x.endswith() 作用：判断字符串是否以指定字符或子字符串开头
# s = 'jr_shenjing'
# print(s.endswith('shenjing'))



# x.endswith()作用：判断字符串是否以指定字符或子字符串开头
# names=['albert','jr_shenjing','kobe','kd']
# # names=[len(name) for name in names if not name.endswith('shenjing')]
# # print(names)
# for name in names:
#     if not name.endswith('shenjing'):
#         print(name)


# yield
# def test_yield():
#     print('first')
#     yield 1
#     print('second')
#     yield 2
#     print('third')
#     yield 3
#
# res = test_yield()
# print(res)
# print(res.__iter__() is res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

# 自定义range
# def show_my_range(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
# for item in show_my_range(1, 10, 3):
#     print(item)


# Python文件
# import spam

# print(spam)
#
# print(spam.money)
# spam.read1()
#
# money = 1
# print(spam.money)

# read1 = 2
# read2 = 3

# spam.read1()
# spam.read2()
# print()
# spam.change()
# spam.read1()

# from...import....
# from spam import *
# # print(money)
# # print(read1)
# # print(read2)

# from spam import *
# # print(money)

# 全局作用域
# global_count = 0
#
# def global_check():
#     print(global_count)
#
# def global_modify():
#     global global_count
#     global_count += 1
#     print(global_count)
#
# global_check()
# global_modify()

# 局部作用域
# def make_counter():
#     count = 0
#
#     def check_counter1():
#         print(count)
#
#         def check_counter2():
#             print(count)
#
#         check_counter2()
#
#     check_counter1()
#
#     def modify_counter():
#         nonlocal count
#         count += 1
#         print(count)
#
#     modify_counter()
#
# make_counter()

# def bar():
#     print('Yes')
#
# f = bar
# f()
#
# def bar():
#     print('Yes')
#
# def wrapper(func):
#     func()
#
# wrapper(bar)

# z = 1
# l = [z,]
# print(l)

# def get():
#     pass
#
# def put():
#     pass
#
# l1 = [get, put]
# print(l1)
# l1[0]()



# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print('from inner:', x)
#
#     return inner
#
# f = outer()
# f()

# * 打散作用
# def foo(x,y,z,*args):
#     print(x,y,z,args)
#
# foo(1,2,3,4,5,6)

# def foo(x,y,z,*args):
#     print(x,y,z)
#     print(args)

# foo(1,2,3,*[4,5,6,7,8])
# foo(1,2,3,*(4,5,6,7,8))
# foo(1,2,3,'hello')
# foo(1,2,3,*'hello')



# **打散
# def foo(x,y,z,**kwargs):
#     print(x,y,z)
#     print(kwargs)
#
# foo(1,2,3,**{'a':4,'b':5})
# foo(1,2,3, a=4, b=5)

# def boo(x,y,z):
#     print(x,y,z)
#
# boo(1, **{'z':3, 'y':2})



# def sum2(*args):
#     res = 0
#     for num in args:
#         res += num
#     return res
#
# r = sum2(1,2,3,4,5,6,7)
# print(r)


# def index(name, age, gender):
#     print('welcome %s %s %s'%(name, age, gender))
#
# def wrapper(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     index(*args, **kwargs)
#
# # wrapper(1,2,3,a=1,b=2,c=3)
# wrapper(name='Albert', age=18, gender='male')
# warpper('Albert', age=18, gender='male')

# *args放前面约束了
# def auth(*args, name ,pwd):
#     print(name, pwd)
#
# auth(pwd='123', name='Albert')
# auth('123','Ablert')



# def auth(name ,pwd):
#     print(name, pwd)
#     print(type(name))
#
# auth(pwd='123', name='Albert')
# auth('123','Ablert')

# 三元表达式
# x = 12
# y = 13
#
# res = x if x > y else y
# print(res)

# 递归
# def get(n):
#     if n == 1:
#         return 18
#     return get(n-1)+2
#
# s = get(5)
# print(s)

# 匿名函数
# res = lambda x,n: x**n
# print(res)
# print(res(2,2))

# re = lambda x,y: x+y
# print(re)
# print(re(1,2))

# print(sorted([2,5,4,6], reverse=True))
# print(max([3,5,43,]))

# 联合 匿名函数和max一起使用
# salaries = {
#     'james': 30000,
#     'kd': 1000,
#     'zi': 10000
# }
#
# print(max(salaries, key=lambda x: salaries[x]))

# 映射
# nums = [3,4,6,7]
# new_nums = map(lambda x: x**2, nums)
# print(list(new_nums))

# names = ['J', 'S', 'A']
# new_names = map(lambda x: x+'test', names)
# print(list(new_names))

# from functools import reduce
# re = reduce(lambda x, y: x + y, range(1, 101), 0)
# print(re)

# list1 = ['today', 'is','the', 'first', 'day', 'of', 'the', 'rest', 'of', 'your', 'life', '.']
# re = reduce(lambda x, y: x + ' '+ y + ' ', list1)
# print(re)

# ages = [10,11,12,13,14,15,16]
# # re = filter(lambda n:True if n < 12 else False, ages)
# re = filter(lambda n: n < 12, ages)
# print(list(re))

# print('a'.zfill(10))
# print('{:.5f}'.format(3.2423243))
# print('{:,}'.format(123123123123))

# re = eval('2*3')
# print(re)
# re1 = eval('[1,2,3,4]')
# print(re1)
# re2 = eval('{"name":"albert", "age":18}')
# print(re2)

# s = {1,2,3}
# s.add(5)
# print(s)
# frozenset({s})
# s.add(6)

# print(hash('a'))
# print(hash((12,3,4)))
# print(pow(2,3,3))
# print(round(3,5))

# left = 'hello'
#
# right1 = {'x':1, 'y':2, 'z':3}
# right2 = [1,2,3,4,5]
#
# re = zip(left, right1)
# print(list(re))

# re = [i for i in range(1,101) if i%2==0]
# print(re)

# re = (i for i in range(0,101) if i%2==0)
# print(re)
# for i in range(1,4):
#     print(re.__next__())

# 内置函数
# print(print)

# 全局作用域
# globals_count = 0
#
# def global_modify():
#     global globals_count
#     globals_count = 1
#     print(globals_count)
#
# global_modify()

# 局部作用域
# def make_counter():
#     count = 0
#
#     def modify_counter():
#         nonlocal count
#         count = 1
#         print(count)
#
#     modify_counter()
#
# make_counter()

# 闭包函数
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print(x)
#     return inner
#
# f = outer()
# print(f)

# 闭包函数
# def outer():
#     name = 'albert'
#     def inner():
#         print('my name is {}'.format(name))
#     return inner
#
# f = outer()
# print(f)
# f()

# import os
#
# def modify_file(file_name, old_content, now_content):
#     with open(file_name, mode='r', encoding='utf-8') as read_f,\
#         open('%s.swap'%file_name, mode='w', encoding='utf-8') as write_f:
#         for line in read_f:
#             if old_content in line:
#                 line = line.replace(old_content, now_content)
#
#             write_f.write(line)
#     os.remove(file_name)
#     os.rename('%s.swap'%file_name, file_name)


# def calculate_count(data_str):
#     dict_count = {'alpha':0, 'number':0, 'space':0, 'other':0}
#     for i in data_str:
#         if i.isalpha():
#             dict_count['alpha'] += 1
#         elif i.isdigit():
#             dict_count['number'] += 1
#         elif i is ' ':
#             dict_count['space'] += 1
#         else:
#             dict_count['other'] += 1
#     return dict_count


# names = ['dfxcv','weuy', 'sdfjl', 'wuo']
# NAMES = [i.capitalize() for i in names]
# print(NAMES)
# print(list(map(lambda x:x.capitalize(), names)))


# names = ['dfxcv','weuy', 'sdfjl', 'wuo', 'dfs_shenjing']
# for i in range(len(names)):
#     if names[i].endswith('shenjing')>0:
#         names.pop(i)
# names_lens = [len(i) for i in names]
# print(names_lens)

# names = ['dfxcv','weuy', 'sdfjl', 'wuo', 'dfs_shenjing']
# names_list = list(filter(lambda x: not x.endswith('shenjing'), names))
# print(names_list)

# maxnum = 0
# with open('a.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         if len(line.strip()) > maxnum:
#             maxnum = len(line.strip())
# print(maxnum)
#
# with open('a.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(len(max([line.strip() for line in f], key=lambda x:len(x))))

# 定义类
# class DeepshareStudent:
#     school = 'deepshare'
#     print('====>')
#     def __init__(self):
#         print('===init run====>')
#     def learn(self):
#         print('%s is learning'%self)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')

# name_and_func = DeepshareStudent.__dict__
# print(name_and_func)
# print(name_and_func['school'])
# print(name_and_func['learn'])
# name_and_func['learn']()
# 修正
# name_and_func['learn']('albert')

# print(DeepshareStudent.school)
# print(DeepshareStudent.learn)
# print(DeepshareStudent.eat)
# print(DeepshareStudent.sleep)

# print(DeepshareStudent.learn('albert'))

# DeepshareStudent.abc

# 修改属性
# DeepshareStudent.school = 'asd'
# print(DeepshareStudent.school)
#
# # 增加属性
# DeepshareStudent.country = 'city'
# print(DeepshareStudent.country)
#
# # 删除属性
# del DeepshareStudent.country
# print(DeepshareStudent.country)

# 调用类
# DeepshareStudent()

# stu1 = DeepshareStudent()
# print(stu1.school)

# __init__函数
# DeepshareStudent()

# 定义类
# class DeepshareStudent:
#     school = 'deepshare'
#     def __init__(self, x, y, z):
#         self.NAME = x
#         self.AGE = y
#         self.GENDER = z
#     def learn(self):
#         print('%s is learning'%self)
#     def eat(self):
#         print('is eating')
#     def sleep(self):
#         print('is sleeping')
#
# stu1 = DeepshareStudent('albert', 18, 'male')
# print(stu1.school)
# print(stu1.NAME)

# 闭包函数的练习
# db = 'a.txt'
# login_status = {'status':False}
#
# def auth(auth_type = 'file'):
#     def auth2(func):
#         def wrapper(*args, **kwargs):
#             if login_status['status']:
#                 return func(*args, **kwargs)
#             if auth_type == 'file':
#                 with open(db, encoding='utf-8') as f:
#                     dic = eval(f.read())
#                 name = input('username:').strip()
#                 password = input('password').strip()
#                 if name == dic['name'] and  password == dic['password']:
#                     login_status['status'] = True
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('username or passwrod error')
#             elif auth_type == 'sql':
#                 pass
#             else:
#                 pass
#
#         return wrapper
#
#     return auth2
#
# @auth()
# def index():
#     print('index')
#
# @auth(auth_type='file')
# def home(name):
#     print('welcome %s to home'%name)
#
# index()
# home('albert')

# 闭包函数练习2
# import time
# import random
#
# user_data = {
#     'user':None,
#     'login':False,
#     'now_time':time.time()
# }
# db_username = 'albert'
# db_password = '123'

# time.sleep(2)
# passed_time = time.time() - user_data['now_time']
# print(passed_time)

# now_time = time.time()
# time.sleep(2)
# pass_time = time.time()
# l_time = pass_time - now_time
# print(l_time)

# def auth(func):
#     def wrapper(*args, **kwargs):
#         passed_time = time.time() - user_data['now_time']
#
#         if user_data['user'] and passed_time < 3:
#             return func(*args, **kwargs)
#         else:
#             while True:
#                 username = input('input your username>>:').strip()
#                 password = input('input your password>>:').strip()
#                 if username == db_username and password == db_password:
#                     print('login sucessfully')
#                     user_data['user'] = username
#                     user_data['login'] = True
#                     user_data['now_time'] = time.time()
#                     return func(*args, **kwargs)
#                 else:
#                     print('username or password is invalid')
#
#     return wrapper
#
# @auth
# def index():
#     print('This is index page')
#
# @auth
# def home(name):
#     print('welcome %s to home page'%name)
#
# index()
# time.sleep(random.randint(2,4))
# home('albert')

# 闭包函数 练习3
# import time
#
# def add_log(file):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             with open(file, 'a', encoding='utf-8') as f:
#                 f.write('[%s]:[%s]\n'%(func.__name__, time.strftime('%Y-%m-%d %X')))
#                 return func(*args, **kwargs)
#
#         return inner
#
#     return wrapper
#
# @add_log('db1.txt')
# def index():
#     print('This is index page')
#
# @add_log('db2.txt')
# def home(name):
#     print('Welcome %s to home page '% name)
#
# index()
# home('albert')

# 第3条
# Pthon3中，我们需要编写接收str或bytes，并总是返回str的方法：
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str, bytes):
#         value = bytes_or_str.decode('utf-8')
#     else:
#         value = bytes_or_str
#     return value

# 迭代器
# dict1 = {'x':1, 'y':2, 'z':3}
# iter_dict1 = dict1.__iter__()
# print(iter_dict1.__next__())
# print(iter_dict1.__next__())
# print(iter_dict1.__next__())
# print(iter_dict1.__next__())

# str1 = 'hello'
# iter_dict1 = str1.__iter__()
# print(iter_dict1.__next__())
# print(iter_dict1.__iter__() is iter_dict1)

# def test_yield():
#     print('======>first')
#     yield 1
#     print('======>second')
#     yield 2
#     print('======>third')
#     yield 3
#
# print(test_yield)
# res = test_yield()
# print(res)
# print(res.__iter__() is res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

# def show_my_range(start, stop, step=1):
#     n = start
#     while n < stop:
#         yield n
#         n += step
#
# res = show_my_range(1, 10)
# print(res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
#
# for i in show_my_range(1,10):
#     print(i)

# def eat(name):
#     print('[1] %s is ready for eating'%name)
#     while True:
#         food = yield
#         print('[2] %s starts to eat %s'%(name, food))
#
# person1 = eat('Albert')
# print(person1)
# person1.__next__()
# person1.__next__()
# person1.__next__()
# person1.__next__()

# import math
#
# def my_sqrt(num):
#     if num < 0: print("请输入大于0")
#     elif num < 1: return 0
#     elif 1 < num < 2: return 1
#     else:
#         l, h = 0, num
#         while l <= h:
#             m = math.floor((l + (h - l))/2)
#             if num/m > m:
#                 l = m + 1
#             elif num/m < m:
#                 h = m - 1
#             else:
#                 return m
#     return h


# from collections import namedtuple
# point = namedtuple('p', ['x', 'y'])
# p = point(1, 2)
# print(p)
# print(type(p))

# from collections import ChainMap
# dict1 = {'name': 'Albert', 'age': 18}
# dict2 = {'weight':65, 'height':180}
# res = list(ChainMap(dict1, dict2))
# print(res)

# 过滤
# ages = [1,2,3,4,5,6,7]
# res = filter(lambda m: True if m >= 3 else False, ages)
# print(list(res))

# res = '{}, {}, {}'.format('age', 18, 'name')
# print(res)
# print(type(res))

# res = '{0}, {1}, {0}'.format('age', 18, 'name')
# print(res)

# res = '{name}, {age}, {sex}'.format(age=18, sex='male', name='Albert')
# print(res)

# print("{:>10}".format('18'))
# print("{:3>18}".format('18'))
#
# print('a'.zfill(10))
# print('{:.5f}'.format(3.141516))
#
# print("{:b}".format(18))

# print(bin(11))
# print(oct(11))
# print(hex(11))
#
# print(bool(0))

# set_a = {1,2,3,4}
# set_a.add(5)
# print(set_a)


# 组合表达式
# dict = {'a':1,
# #         'b':2,
# #         'c':3}
# #
# # print(max(dict, key=lambda x:dict[x]))


# 映射
# nums = [1, 2, 3, 4, 5]
# res = map(lambda x:x**2, nums)
# print(list(res))

# names = ['Jam', 'Har', 'Cur']
# res = map(lambda x:x+' is super star', names)
# print(list(res))

# 合并
# from functools import reduce
# res = reduce(lambda x, y: x+y,range(1,101),0)
# print(res)

# list1 = ['1', '2', '3', '4']
# res = reduce(lambda x, y: x + ' ' + y + ' ',list1)
# print(res)


# 过滤
# ages = [18, 19, 20, 21, 22]
# res = filter(lambda n:n >20 , ages)
# print(list(res))


# 拉链函数
# left = 'hello'
# right1 = {'x':1, 'y':2, 'z':3}
# right2 = [1,2,3,4,5]
#
# res1 = zip(left, right2)
# print(list(res1))


# 列表
# a = [0 for i in range(26)]
# print(a)

# any() all()
# print(any([1,0,0,0]))
# print(all([1,0,0,0]))

# 字典 any()
# dict = {'a':0,
#         'b':0,
#         'c':0}
# print(any(dict.values()))

# pop()
# a = [1,2,3,4]
# print(a.pop())


