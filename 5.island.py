# -*- coding: cp936 -*-
from collections import deque

def islandCounter(M):
    if M == None or M == [[]]:
        return 0
    island = 0
    r = len(M)
    c = len(M[0])
    for i in range(0, r):
        for j in range(0, c):
            if M[i][j] == 1:
                island +=1
                findparsofisland(M, i, j, r, c)
    return island

def findparsofisland(M, i, j, r, c):
    q = deque()
    q.append([i, j])
    while len(q)!=0:
        i = q.pop()
        x = i[0]
        y = i[1]
        if M[x][y] == 1:
            M[x][y] = 2
        appendIF(q, r, c, x+1, y) #左侧
        appendIF(q, r, c, x, y+1) #右侧
        appendIF(q, r, c, x-1, y) #下方
        appendIF(q, r, c, x, y-1) #上方
            

def appendIF(q, r, c, x, y):
    if x>=0 and x<c and y>=0 and y<r:
        q.append([x, y])

M = [[1,0,1],
     [0,1,1]]

s = islandCounter(M)
print(s)
