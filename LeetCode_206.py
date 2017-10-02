#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LeetCode_206.py
# @Author: UpTownCat
# @Date  : 2017/10/2

class ListNode(object):
    def __init__(self, v):
        self.val = v
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        # pointer = head
        # while pointer.next.next:
        #     pointer = pointer.next
        # root = pointer.next
        # pointer.next = None
        # root.next = self.reverseList(head)
        # return root
        l = []
        while head:
            l.append(head)
            head = head.next
        l.reverse()
        l.append(None)
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
solution = Solution()
root = solution.reverseList(head)
# reduce(lambda : 1 + 1, [])
while root:
    print(root.val)
    root = root.next