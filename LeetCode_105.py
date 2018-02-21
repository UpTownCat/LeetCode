# Definition for a binary tree node.
from utils import Utils
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        left_pre_bound = 1+inorder.index(preorder[0])
        left_pre = preorder[1:left_pre_bound]
        right_pre = preorder[left_pre_bound:]
        in_bound = inorder.index(preorder[0])
        left_in = inorder[:in_bound]
        right_in = inorder[in_bound+1:]
        head.left = self.buildTree(left_pre, left_in)
        head.right = self.buildTree(right_pre, right_in)
        return head

solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree = solution.buildTree(preorder, inorder)
Utils.print_binary_tree(tree)