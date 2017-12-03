# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue1 = [root]
        queue2 = []
        result = []
        while queue1 or queue2:
            res = []
            if queue1:
                for node in queue1:
                    res.append(node.val)
                    # add subnode to another queue
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
                # clear
                queue1 = []
            else:
                for node in queue2:
                    res.append(node.val)
                    if node.left:
                        queue1.append(node.left)
                    if node.right:
                        queue1.append(node.right)
                queue2 = []
            result.append(res)
        return result

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

root_left.left = root_right_left
root_left.right = root_right_right

solution = Solution()

print solution.levelOrder(root)
