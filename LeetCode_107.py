# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, q1, q2 = [], [], []
        q1.append(root)
        while q1 or q2:
            r = []
            if q1:
                for item in q1:
                    r.append(item.val)
                    if item.left:
                        q2.append(item.left)
                    if item.right:
                        q2.append(item.right)
                q1 = []
            else:
                for item in q2:
                    r.append(item.val)
                    if item.left:
                        q1.append(item.left)
                    if item.right:
                        q1.append(item.right)
                q2 = []
            res.append(r)
        res.reverse()
        return res

root = TreeNode(3)

root_left = TreeNode(9)

root_right = TreeNode(20)
root.left = root_left
root.right = root_right

root_right_left = TreeNode(15)
root_right_right = TreeNode(7)

root_left_left = TreeNode(15)
root_left_right = TreeNode(7)

root_right.left = root_right_left
root_right.right = root_right_right

# root_left.left = root_right_left
# root_left.right = root_right_right

solution = Solution()

print solution.levelOrderBottom(root)
