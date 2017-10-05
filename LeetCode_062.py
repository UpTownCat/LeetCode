#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_062.py
# @Author: UpTownCat
# @Date  : 2017/10/5
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(0, n)] for i in range(m)]
        dp[0] = [1 for j in range(n)]
        for i in range(1, m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]
solution = Solution()
print(solution.uniquePaths(1, 4))