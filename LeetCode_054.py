#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_054.py
# @Author: UpTownCat
# @Date  : 2017/10/3
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n, v, h, results = len(matrix), len(matrix[0]), 0, 0, []
        if m == 1:
            for i in matrix[0]:
                results.append(i)
            return results
        if n == 1:
            for i in range(len(matrix)):
                results.append(matrix[i][0])
            return results
        while v < int(m / 2) and h < int(n / 2):
            for i in range(h, n - h - 1):
                results.append(matrix[v][i])
            for i in range(v, m - v - 1):
                results.append(matrix[i][n - h - 1])
            for i in range(n - h - 1, h, -1):
                results.append(matrix[m - v - 1][i])
            for i in range(m - v - 1, v, -1):
                results.append(matrix[i][v])
            h, v = h + 1, v + 1
        if (m % 2 == 1 or n % 2 == 1) and m != 2 and n != 2:
            if m < n and m % 2 != 0:
                for x in range(h, n - h):
                    results.append(matrix[v][x])
            if m >= n and n % 2 != 0:
                for x in range(v, m - v):
                    results.append(matrix[x][h])
        return results
# for i in range(9, 0, -1):
#     print(i)
solution = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
print(solution.spiralOrder(matrix))