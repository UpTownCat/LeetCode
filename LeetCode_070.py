#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_070.py
# @Author: UpTownCat
# @Date  : 2017/10/5

#爬楼梯
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        pre1, pre2 = 1, 2
        for i in range(3, n + 1):
            pre1, pre2 = pre2, pre1 + pre2
        return pre2
solution = Solution()
print(solution.climbStairs(4))
