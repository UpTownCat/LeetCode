#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_074.py
# @Author: UpTownCat
# @Date  : 2017/10/6

#二维数组搜索（二分查找）
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = int((left + right) / 2)
            i, j = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid
        return False
