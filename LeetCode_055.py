#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_055.py
# @Author: UpTownCat
# @Date  : 2017/10/4

class Solution(object):
    def canJump(self, nums):
        if not nums or 0 not in nums:
            return True
        zeroCount = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0 and zeroCount == 0:
                zeroCount = 1
                continue
            if zeroCount > 0:
                if nums[i] <= nums[i + 1] + 1:
                    zeroCount += 1
                else:
                    zeroCount = 0 if nums[i] >= zeroCount + 1 else zeroCount + 1
        return zeroCount == 0

nums = [2, 0, 2]
solution = Solution()
print(solution.canJump(nums))