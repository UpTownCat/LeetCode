# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        head = TreeNode(postorder[-1])
        in_bound = inorder.index(postorder[-1])
        left_in = inorder[:in_bound]
        right_in = inorder[in_bound+1:]
        left_post = postorder[:in_bound]
        right_post = postorder[in_bound:-1]
        head.left = self.buildTree(left_in, left_post)
        head.right = self.buildTree(right_in, right_post)
        return head