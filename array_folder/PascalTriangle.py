#!/usr/bin/env python  
# encoding: utf-8     
""" 
@version: v1.0 
@author: Jerry 
@software: PyCharm 
@file: PascalTriangle.py 
@time: 2017/3/30 21:59 
"""


class Solution(object):
    def generate(self, numRows):
        lists = []

        for i in range(numRows):
            lists.append([1] * (i + 1))
            if numRows<=1:
                return lists[numRows]
            if i > 1:
                for j in range(1, i):
                    lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
        return lists[numRows-1]


if __name__ == '__main__':

    slists = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    solution = Solution()
    print(solution.generate(numRows=5))
