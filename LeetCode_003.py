#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_003.py
# @Author: UpTownCat
# @Date  : 2017/10/1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        pointer = None
        up = 0
        while l1 != None:
            v1 = l1.val
            v2 = 0
            if l2 != None:
                v2 = l2.val
            if l3 == None:
                l3 = ListNode((v1 + v2 + up) % 10)
                pointer = l3
            else:
                pointer.next = ListNode((v1 + v2 + up) % 10)
                pointer = pointer.next
            up = int((v1 + v2 + up) / 10)
            l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if up != 0:
            if l2 == None:
                pointer.next = ListNode(up)
                pointer = pointer.next
            else:
                while up != 0 and l2 != None:
                    val = up + l2.val
                    pointer.next = ListNode(val % 10)
                    pointer = pointer.next
                    up = int(val / 10)
                    l2 = l2.next
                if up != 0:
                    l2 = ListNode(up)
        if l2 != None:
            pointer.next = l2
        if l3 == None:
            return ListNode(0)
        return l3