#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class MyQueue:

    def __init__(self):
        """
        defInitialize your data structure here.
        """
        # 初始化两个列表,当作栈来使用
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        # 队列的push操作
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        # 队列的pop操作
        self.stack.pop(0)

    def peek(self):
        """
        Get the front element.
        """
        self.stack.peek(0)

    def empty(self):
        """
        Returns whether the queue si empty.
        """
        return self.stack == []
