class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for v in s:
            if v in d:
                stack.append(v)
            else:
                if not stack or d[stack.pop()] != v:
                    return False
        return not stack

s = '{{[[]]})}()'
solution = Solution()
print solution.isValid(s)