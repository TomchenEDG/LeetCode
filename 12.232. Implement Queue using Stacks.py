#!/usr/bin/env python 
# -*- coding:utf-8 -*-



class MyQueue:

    def __init__(self):
        """
        defInitialize your data structure here.
        """
        # 初始化两个列表,当作栈来使用
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        # 队列的push操作
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        # 队列的pop操作
        if self.stack_out:
            return self.stack_out.pop()
        else:
            # 将stack-in的数据全部push进stack-out中,然后stack_out的顺序和队列pop的顺序一致
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        """
        if self.stack_out:
            return self.stack_out[-1]
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue si empty.
        """
        return not self.stack_in and not self.stack_out


def main():

    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    queue.peek()
    queue.pop()
    queue.empty()


if __name__ == '__main__':main()
