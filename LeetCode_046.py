class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        self.handle(nums, 0, result)
        return result

    def handle(self, nums, k, result):
        n = len(nums)
        if k == n:
            result.append(nums[:])
            return
        for i in range(k, n):
            nums[k], nums[i] = nums[i], nums[k]
            self.handle(nums, k+1, result)
            nums[k], nums[i] = nums[i], nums[k]

nums = [1, 2, 3]
solution = Solution()
result = solution.permute(nums)
print result