# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            left = root.left
            root.left = None
            right = root.right
            self.flatten(left)
            root.right = left
            pointer = root
            while pointer.right:
                pointer = pointer.right
            self.flatten(right)
            pointer.right = right

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
root.right = n2

solution = Solution()
solution.flatten(root)

while root:
    print(root.val)
    root = root.right