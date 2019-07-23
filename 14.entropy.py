#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# 第一种：假设一组信息中有两个类别，那么当一个类别所占比例为x时，另一个类别的所占比例肯定是1−x.
import numpy as np
import matplotlib.pyplot as plt

def entropy(p):
    return -p*np.log(p) -(1-p)*np.log(1-p)

x = np.linspace(0.01, 0.99, 200)

plt.plot(x, entropy(x))
plt.show()



# 第二种：条件熵
from collections import Counter

def entropy(y):
    counter = Counter(y)
    res = 0.0
    for num in counter.values():
        p = num / len(y)
        res += -p * log(p)
    return res
