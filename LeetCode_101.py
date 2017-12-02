# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.handle(root.left, root.right)

    def handle(self, left_root, right_root):
        # situation one
        if not left_root and not right_root:
            return True
        # situation two
        if (not left_root and right_root) or (left_root and not right_root):
            return False
        # situation three
        if left_root.val != right_root.val:
            return False
        return self.handle(left_root.left, right_root.right) and self.handle(left_root.right, right_root.left)