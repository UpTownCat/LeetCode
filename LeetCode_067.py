#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_067.py
# @Author: UpTownCat
# @Date  : 2017/10/5
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry, result = len(a) - 1, len(b) - 1, 0, ''
        while i >= 0 or j >= 0 or carry > 0:
            v1, v2 = 0, 0
            if i >= 0:
                v1 = int(a[i])
            if j >= 0:
                v2 = int(b[j])
            v = v1 + v2 + carry
            carry, v = divmod(v, 2)
            result += str(v)
            i, j = i - 1, j - 1
        return result[::-1]
solution = Solution()
print(solution.addBinary('1010', '1011'))