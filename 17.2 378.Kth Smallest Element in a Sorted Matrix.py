#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/13 0013 13:45 
# @Autohor: Sam
# @File   : 378. Kth Smallest Element in a Sorted Matrix.py



# 第二种：堆解法，较二分法较慢
# matrix = [[ 1,  5,  9],
#           [10, 11, 13],
#           [12, 13, 15]]
# k = 8
#
# import heapq
# def kthSmallest(matrix, k):
#
#     m, n = len(matrix), len(matrix[0])
#     h = []
#
#     for i in range(n):
#         heapq.heappush(h, (matrix[0][i], 0, i))
#     for i in range(k - 1):
#         item = heapq.heappop(h)
#         if item[1] + 1 < m:
#             heapq.heappush(h, (matrix[item[1] + 1][item[2]], item[1] + 1, item[2]))
#
#     return heapq.heappop(h)[0]
#
# # 运行
# a = kthSmallest(matrix,k)
# print(a)







# # 学习使用：手动实现堆排序
def kthSmallest(matrix, k):
    # 此题方法和23. 合并K个排序链表 相似
    # 采用堆排序
    def adjustHeap(heap, start, end):
        dad = start
        son = dad * 2 + 1
        while son < end:
            x = matrix[heap[dad][0]][heap[dad][1]]
            y1 = matrix[heap[son][0]][heap[son][1]]
            if son + 1 < end:
                y2 = matrix[heap[son + 1][0]][heap[son + 1][1]]
                if y2 < y1:
                    son = son + 1
                    y1 = matrix[heap[son][0]][heap[son][1]]
            if x > y1:
                tmp = heap[dad]
                heap[dad] = heap[son]
                heap[son] = tmp
                dad = son
                son = dad * 2 + 1
            else:
                return

    n = len(matrix)

    heap = []
    for i in range(0, n):
        heap.append([i, 0])

    # 初始化堆
    t = n // 2 - 1
    while True:
        if t < 0:
            break
        adjustHeap(heap, t, n)
        t = t - 1

    for i in range(0, k - 1):
        tmp = heap.pop(0)
        if tmp[1] + 1 < n:
            heap.insert(0, [tmp[0], tmp[1] + 1])
            adjustHeap(heap, 0, len(heap))
        else:
            a = heap.pop()
            heap.insert(0, a)
            adjustHeap(heap, 0, len(heap))

    return matrix[heap[0][0]][heap[0][1]]


matrix = [[ 1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8

a = kthSmallest(matrix,k)
print(a)