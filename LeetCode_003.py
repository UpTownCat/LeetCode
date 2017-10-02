#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_003.py
# @Author: UpTownCat
# @Date  : 2017/10/1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mac = 1
        right = 1
        left = 0
        length = len(s)
        while left < length:
            while right < length:
                index = left
                tag = 0
                while index < right:
                    if s[index] == s[right]:
                        mac = max(mac, right - left)
                        left = index + 1
                        tag = 1
                        break
                    index = index + 1
                right = right + 1
                if tag:
                    break
            if right == length:
                mac = max(mac, right - left)
                break
        if len(s) == 0:
            mac = 0
        return mac