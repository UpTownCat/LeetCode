class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex+1):
            pre = 1
            for j in range(1, i):
                pre, res[j] = res[j], res[j]+pre
            res.append(1)
        return res

solution = Solution()
print(solution.getRow(1))