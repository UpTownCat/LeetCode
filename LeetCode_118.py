class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            sub = []
            for j in range(i+1):
                if j == 0 or i == j:
                    sub.append(1)
                else:
                    sub.append(res[i-1][j-1]+res[i-1][j])
            res.append(sub)
        return res