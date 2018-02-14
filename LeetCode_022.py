class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parentheses = ['(', ')']
        result = []
        def process(n1, n2, s):
            if n1 == 0 and n2 == 0:
                result.append(''.join(s))
                return
            if n1 == n2:
                s.append(parentheses[0])
                process(n1 - 1, n2, s)
                del s[-1]
            elif n1 < n2:
                if n1 > 0:
                    s.append(parentheses[0])
                    process(n1 - 1, n2, s)
                    del s[-1]
                s.append(parentheses[1])
                process(n1, n2 - 1, s)
                del s[-1]
        process(n, n, [])
        return result

solution = Solution()
print(solution.generateParenthesis(3))