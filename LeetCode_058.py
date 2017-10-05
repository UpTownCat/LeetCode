#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_058.py
# @Author: UpTownCat
# @Date  : 2017/10/4
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[len(s) - 1] == ' ':
            return 1
        length = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                length = len(s) - i - 1
                break
        return length
solution = Solution()
s = 'hello world'
print(solution.lengthOfLastWord('a '))