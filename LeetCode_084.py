class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        max_area = 0
        for i, val in enumerate(heights):
            if not stack or heights[stack[-1]] <= val:
                stack.append(i)
            else:
                while(stack and heights[stack[-1]] > val):
                    min_height = stack.pop()
                    left = stack[-1] if stack else -1 # if stack is empty that is to say the current index is min of heights
                    max_area = max(max_area, heights[min_height] * (i - left - 1))
                stack.append(i)
        heights.pop()
        return max_area
solution = Solution()
heights = [6]
print(solution.largestRectangleArea(heights))
