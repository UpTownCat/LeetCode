#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_069.py
# @Author: UpTownCat
# @Date  : 2017/10/5
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        if x < 1:
            return 0
        left, right = 0, x
        while left < right:
            mid = int((left + right) / 2)
            if mid * mid > x:
                right = mid
            elif (mid + 1) * (mid + 1) > x:
                return int(mid)
            else:
                left = mid + 1
        return 0
solution = Solution()
print(solution.mySqrt(4))