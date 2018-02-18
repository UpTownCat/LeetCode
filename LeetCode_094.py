# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        if not root:
            return []
        if root.left:
            nodes.extend(self.inorderTraversal(root.left))
        nodes.append(root.val)
        if root.right:
            nodes.extend(self.inorderTraversal(root.right))

        return nodes

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2

solution = Solution()
res = solution.inorderTraversal(root)
print(res)