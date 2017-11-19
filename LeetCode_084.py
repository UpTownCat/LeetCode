class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        max_area = 0
        left = []
        right = []

        return max_area

solution = Solution()
heights = [6, 2, 5, 4, 5, 1, 6]
print(solution.largestRectangleArea(heights))
