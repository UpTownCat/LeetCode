#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_004.py
# @Author: UpTownCat
# @Date  : 2017/10/1

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if m == 0:
            if n % 2 == 1:
                return nums2[int(n/2)] * 1.0
            mid = int(n / 2)
            return (nums2[mid] + nums2[mid - 1]) / 2
        i_left, i_right = 0, m + 1
        while i_left < i_right:
            i = int((i_left + i_right) / 2)
            j = int((n + m + 1) / 2) - i
            if (i == 0 and nums2[j - 1] <= nums1[i]) or (i == m and nums1[i - 1] <= nums2[j]) or (j == n and nums2[j - 1] <= nums1[i]) or (j == 0 and nums1[i - 1] < nums2[j]) or (nums1[i - 1] <= nums2[j] and nums2[j - 1] <= nums1[i]):
                if i == 0:
                    if j != n:
                        max_left, min_right = nums2[j - 1], min(nums1[i], nums2[j])
                    else:
                        max_left, min_right = nums2[j - 1], nums1[i]
                    # return (nums2[j - 1] + min(nums1[i], nums2[j])) / 2
                elif i == m:
                    if j != 0:
                        max_left, min_right = max(nums1[i - 1], nums2[j - 1]), nums2[j]
                    else:
                        max_left, min_right = nums1[i - 1], nums2[j]
                    # return (max(nums1[i - 1], nums2[j - 1]) + nums2[j]) / 2
                else:
                    max_left, min_right = max(nums1[i - 1], nums2[j - 1]), min(nums1[i], nums2[j])
                    # return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2
                if (n + m) % 2 == 1:
                    return max_left * 1.0
                return (max_left + min_right) / 2 * 1.0
            elif nums1[i - 1] > nums2[j]:
                i_right = i
            else:
                i_left = i + 1


def binarySearch(l, target):
    left = 0
    right = len(l)
    while left < right:
        mid = int((left + right) / 2)
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == '__main__':
    print(binarySearch(l, 8))
    nums1 = [1, 2]
    nums2 = [3, 4]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
