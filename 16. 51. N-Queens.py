#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/15 0015 20:15 
# @Autohor: Sam
# @File   : 51. N-Queens.py



# import matplotlib.pyplot as plt
#
# def conflict(ps,pos):
#     """
#     检测新皇后放的位置和之前的皇后在位置上是否有冲突
#     :param ps: 表示之前摆放的皇后位置
#     :param pos:表示新皇后要放的位置
#     :return:有的话返回True,否则，返回False
#     """
#     l=len(ps)
#     for i in range(l):
#         if pos == ps[i] or l-i == abs(pos-ps[i]):
#             return True
#     return False
#
#
# def mou(st):
#     ps=[]
#     for i in st:
#         ps.append(i[0])
#     return ps
#
#
# def queue(num):
#     st=[]
#     for begin in range(num):
#         #和走迷宫一样，begin是开始位置
#         st.append([begin, 0])
#         # 放[begin,2]表示第begin个位置，下一个位置0没有探查
#         while len(st) != 0:
#             ps = mou(st)
#             pos, nxt = st.pop()
#             for nextp in range(nxt, num):
#                 if not conflict(ps, nextp):
#                     st.append((pos, nextp + 1))
#                     st.append((nextp, 0))
#                     if len(st) == num:
#                         #栈的长度达到8,表示已经找到一个结果
#                         ps.append(nextp)
#                         yield ps
#                     break
#     print("搜索完毕")

# num=8
# item=queue(num)
# a=next(item)
# print(a)
# plt.grid()
# plt.scatter(range(num),a,800,a)
# plt.title("8 queen")
# plt.show()

# import random


# 冲突检查，在定义state时，采用state来标志每个皇后的位置，
# 其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
# def conflict(state, nextX):
#     nextY = len(state)
#     #    print(nextY),
#     for i in range(nextY):
#         # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
#         if abs(state[i] - nextX) in (0, nextY - i):
#             # 纵坐标减去下一个皇后的横坐标的绝对值 处于 0到下一皇后纵坐标减i则冲突
#             return True
#     return False



# def conflict(previous_queen, now_queen):
#     """
#     检测新皇后放的位置 和 之前的皇后是否有冲突
#     :param previous_queen: 表示之前摆放的皇后位置
#     :param now_queen: 新皇后要放的位置
#     :return: 有冲突返回True，否则返回False
#     """
#     l = len(previous_queen)
#     for i in range(l):
#         if now_queen == previous_queen[i] or \
#                 l - i == abs(now_queen - previous_queen[i]):
#             return True
#     return False
#
# def mou(st):
#     ps = []
#     for i in st:
#         ps.append(i[0])
#     return ps
#
# def queens(num):
#     st = []
#     for begin in range(num):
#         # begin是开始位置
#         st.append([begin, 0])
#         # 放[begin,2]表示第begin个位置，下一个位置0没有探查
#         while len(st) != 0:
#             ps = mou(st)
#             pos, nxt = st.pop()
#             for nextp in range(nxt, num):
#                 if not conflict(ps, nextp):
#                     st.append((pos, nextp + 1))
#                     st.append((nextp, 0))
#                     if len(st) == num:
#                         # 栈的长度达到8,表示已经找到一个结果
#                         ps.append(nextp)
#                         yield ps
#                     break
#
# item = queens(8)
# print(item.__next__())

# # 为了直观表现棋盘，用X表示每个皇后的位置
# def prettyprint(solution):
#     def line(pos, length=len(solution)):
#         return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
#
#     for pos in solution:
#         print(line(pos))
#
#
# if __name__ == "__main__":  # 来判断是否是在直接运行该.py文件
#     prettyprint(random.choice(list(queens(8))))






# 八皇后问题
class Solution:
    def __init__(self, n):
        """
        初始化
        :param n: 设置N个皇后
        """
        self.chessboard = [0] * n  # 设置行棋盘
        self.solutions = 0    # 记录所有解

    def queens(self, start_position, number_of_queens):
        """
        算出N皇后问题的解
        :param start_position: 从棋盘第几个位置开始
        :param number_of_queens: 设置多少个皇后
        :return: None
        """
        if (start_position == number_of_queens):
            print(self.chessboard) # 打印解
            self.solutions += 1   # 叠加解的次数
            return

        # 遍历每一位皇后
        for queen in range(number_of_queens):
            # 把皇后放在棋盘的位置
            self.chessboard[start_position] = queen
            # 检查通过，则进入棋盘下一个位置进行递归
            if self.conflict(start_position) == True:
                self.queens(start_position + 1, number_of_queens)
        return

    def conflict(self, position):
        """
        # 检查 所放皇后的 横向、 纵向、 斜线，是否有冲突
        :param position: 当前皇后的位置
        :return: 冲突则返回True，否则，返回False
        """
        for i in range(position):
            # 检查 当前皇后的位置在 横向、纵向、斜线，是否有冲突
            if self.chessboard[i] == self.chessboard[position] or \
                    abs(self.chessboard[i] - self.chessboard[position]) == position - i:
                return False
        return True


if __name__ == '__main__':
    res = Solution(4)
    res.queens(0, 4)
    print(res.solutions)