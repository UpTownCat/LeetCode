#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_063.py
# @Author: UpTownCat
# @Date  : 2017/10/5
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        m, n, t1, t2 = 0, 0, 0, 0
        for m in range(len(obstacleGrid)):
            if obstacleGrid[m][0] == 0 and t1 == 0:
                obstacleGrid[m][0] = 2
            else:
                t1, obstacleGrid[m][0] = 1, 0
        for n in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][n] == 0 and t2 == 0:
                obstacleGrid[0][n] = 2
            else:
                t2, obstacleGrid[0][n] = 1, 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    v1, v2 = 0, 0
                    if obstacleGrid[i - 1][j] != 1:
                        v1 = obstacleGrid[i - 1][j]
                    if obstacleGrid[i][j - 1] != 1:
                        v2 = obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] = v1 + v2
        return int(obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] / 2)
solution = Solution()
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(solution.uniquePathsWithObstacles([[0]]))