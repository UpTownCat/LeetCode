#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_053.py
# @Author: UpTownCat
# @Date  : 2017/10/2
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum, m = -2147483647, -2147483647
        for i in range(len(nums)):
            if nums[i] > nums[i] + m:
                m = nums[i]
            else:
                m = nums[i] + m
            maxnum = max(maxnum, m)
        return maxnum

