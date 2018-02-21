# Definition for singly-linked list.
from utils import Utils

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        pointer = head
        n = 0
        while pointer:
            n += 1
            pointer = pointer.next
        def process(root, start, end):
            if end-start <=1:
                return TreeNode(root.val)
            mid = (start+end)/2
            p = root
            for i in range(start, mid-1):
                p = p.next
            t = TreeNode(p.next.val)
            right = p.next.next
            p.next = None
            if root:
                t.left = process(root, start, mid)
            if right:
                t.right = process(right, mid+1, end)
            return t
        return process(head, 0, n)

l = Utils.list_to_linklist([-10,-3,0,1])

solution = Solution()
head = solution.sortedListToBST(l)

Utils.print_binary_tree(head)