# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        nodes = []
        while head:
            node = head
            head = head.next
            node.next = None
            nodes.append(node)
        del nodes[-n]
        root = None
        pointer = None
        for node in nodes:
            if not root:
                root = node
                pointer = node
            else:
                pointer.next = node
                pointer = pointer.next
        return root

solution = Solution()
l = [1, 2, 3, 4, 5]
solution.removeNthFromEnd(l, 2)
print l
