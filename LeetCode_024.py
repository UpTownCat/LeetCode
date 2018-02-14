# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        left_nodes = second_node.next
        first_node.next = None
        second_node.next = first_node
        second_node.next.next = self.swapPairs(left_nodes)
        return second_node