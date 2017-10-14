#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_083.py
# @Author: UpTownCat
# @Date  : 2017/10/14
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        result = pointer = None
        while head:
            if not result:
                result = pointer = ListNode(head.val)
            else:
                pointer.next = ListNode(head.val)
                pointer = pointer.next
            current_v = head.val
            while head.next and current_v == head.next.val:
                head = head.next
            head = head.next
        return result