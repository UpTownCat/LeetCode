class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profix, max_current = 0, 0
        for i in range(1, len(prices)):
            max_current = max(0, max_current+prices[i]-prices[i-1])
            max_profix = max(max_profix, max_current)
        return max_profix