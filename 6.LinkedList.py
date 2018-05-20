# -*- coding: cp936 -*-
'''
Python中没有一个看起来像链接列表的内置数据结构。
值得庆幸的是，在Python中创建表示数据结构的类很容易!

'''
## 下面是一个元素的代码，它将是一个链表中的单个单元:
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
######################################################################################
'''
在继续之前，
请确保您理解了这段代码!我们使用__init__来初始化一个新元素。
元素有一些与之相关联的值(可以是任何东西——一个数字、一个字符串、一个字符等等)，
并且它有一个指向链表中的下一个元素的变量。
'''
## 现在，让我们建立一个LinkedList类:
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """从一个特定的位置获取一个元素。
            假设第一个位置是“1”。
            如果位置不在列表中，返回“None”。"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """在指定位置插入一个新节点。
            假设第一个位置是“1”。
            在3号位置插入。
            第二和第三个元素。"""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    def delete(self, value):
        """删除具有给定值的第一个节点。"""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
######################################################################################
'''这段代码非常相似——我们刚刚建立了一个LinkedList，
它有一个head元素，它是列表中的第一个元素。
如果我们建立一个没有头的新的LinkedList，它将默认为None。

'''
## 太棒了!让我们为LinkedList添加一个方法，使它更有用。
## 该方法将在LinkedList的末尾添加一个新元素。
#    def append(self, new_element):
#        current = self.head
#        if self.head:
#            while current.next:
#                current = current.next
#            current.next = new_element
#        else:
#            self.head = new_element
######################################################################################
'''
同样，这部分非常重要，所以不要仓促完成。将代码逐行执行，确保一切都有意义。
如果LinkedList已经有一个头，那么遍历每个元素的下一个引用直到列表的末尾。
将列表的末尾设置为new_element。或者，如果没有head，您应该将new_element分配给它，什么都不做。
'''

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
