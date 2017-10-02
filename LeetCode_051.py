#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_051.py
# @Author: UpTownCat
# @Date  : 2017/10/2
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        matrix = [[ '.' for i in range(n)] for j in range(n)]
        results = []
        self.findNqueens(matrix, 0, results)
        return results

    def findNqueens(self, matrix, k, results):
        """
        摆放皇后
        :param matrix:
        :param k:
        :return:
        """
        if k == len(matrix):
            result = []
            for l in range(len(matrix)):
                result.append(''.join(matrix[l]))
            results.append(result)
            return
        for i in range(len(matrix[k])):
            if self.checkConflicts(matrix, k, i):
                continue
            matrix[k][i] = 'Q'
            self.findNqueens(matrix, k + 1, results)
            matrix[k][i] = '.'


    def checkConflicts(self, matrix, k, i):
        """
        检测冲突
        :param matrix:
        :param k:
        :param l:
        :return:
        """
        #竖直方向
        for j in range(k):
            if matrix[j][i] == 'Q':
                return True
        #对角线方向
        m, n = k - 1, i - 1
        while m >= 0 and n >= 0:
            if matrix[m][n] == 'Q':
                return True
            m, n = m - 1, n - 1
        m, n = k - 1, i + 1
        while m >= 0 and n < len(matrix):
            if matrix[m][n] == 'Q':
                return True
            m, n = m - 1, n + 1
        return False
# matrix = [[ '.' for i in range(8)] for j in range(8)]
# print(matrix)
solution = Solution()
print(solution.solveNQueens(8))