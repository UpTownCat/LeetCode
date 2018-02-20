# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        cache = []
        def process(head, sum):
            if not head:
                return None
            sum -= head.val
            cache.append(head.val)
            if sum == 0 and not head.left and not head.right:
                result.append(map(lambda x: x, cache))
                cache.pop()
                return None
            process(head.left, sum)
            process(head.right, sum)
            cache.pop()
        process(root, sum)
        return result

root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(8)
n3 = TreeNode(11)
n4 = TreeNode(13)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(2)
n8 = TreeNode(5)
n9 = TreeNode(1)
# n10 = TreeNode(100)
# n2.right = n10
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9

solution = Solution()
print(solution.pathSum(root, 22))
