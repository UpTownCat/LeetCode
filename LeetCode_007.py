class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x)) == 0:
            return None
        x = str(x)
        x = x[::-1]
        symbol = 1
        if x[-1] == "-":
            symbol = -1
            x = x[:len(x)-1]
        i = 0
        while len(x) > i and x[i] == "0":
            i += 1
        if i < len(x):
            x = x[i:]
        res = symbol*int(x)
        if res >= 2147483648 or res < -2147483648:
            res = 0
        return res
solution = Solution()
print solution.reverse('')