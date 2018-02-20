# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        m1 = 999999999
        m2 = 999999999
        if root.left:
            m1 = min(m1, self.minDepth(root.left))
        if root.right:
            m2 = min(m2, self.minDepth(root.right))
        return 1+min(m1, m2)