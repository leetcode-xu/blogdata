#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 17:12
# @Author  : 徐纪茂
# @File    : demo.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
# import functools
# class Solution:
#     def reconstructQueue(self, people):
#         def cmp(a,b):
#             if a[0] > b[0]:
#                 return -1
#             elif a[0] < b[0]:
#                 return 1
#             elif a[1] > b[1]:
#                 return 1
#             elif a[1] < b[1]:
#                 return -1
#             else:
#                 return 0
#         def sort_list(people):
#             temp = sorted(people, key=functools.cmp_to_key(cmp))
#             return temp
#
#         lists = sort_list(people)
#         ls = []
#         for i in lists:
#             ls.insert(i[1], i)
#
#         return ls
#
# Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
import numpy as np
def z_to_rgb(z, rgb, rang):
    n = len(rgb)
    rang = np.linspace(rang[0], rang[-1], n+1)
    index_z = z // (rang[1] - rang[0])
    i_j = np.zeros(index_z.shape)
    for i, row in enumerate(index_z):
        for j, col in enumerate(row):
            col = int(col)
            if col == n:
                i_j[i][j] = rgb[col-1]
            else:
                i_j[i][j] = rgb[col]
    print(i_j)


if __name__ == '__main__':
    z = np.arange(1, 10)
    z = np.reshape(z, (3, 3))
    rang = [1, 16]
    rgb = np.array([11, 22, 33, 44, 55])
    z_to_rgb(z, rgb, rang)

