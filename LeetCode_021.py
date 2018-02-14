# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        root = l1
        pointer = l1
        l1 = l1.next
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
                pointer = pointer.next
            else:
                pointer.next = l2
                l2 = l2.next
                pointer = pointer.next
        if l1:
            pointer.next = l1
        else:
            pointer.next = l2
        return root