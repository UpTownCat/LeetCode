#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_072.py
# @Author: UpTownCat
# @Date  : 2017/10/6

#两个字符串的编辑距离
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word2 or not word1:
            return len(word1) if not word2 else len(word2)
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j] + 1)
        return dp[m][n]
solution = Solution()
print(solution.minDistance('ab', 'bc'))