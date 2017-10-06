#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_064.py
# @Author: UpTownCat
# @Date  : 2017/10/5
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
grid = [[1, 2], [1, 1]]
solution = Solution()
print(solution.minPathSum(grid))