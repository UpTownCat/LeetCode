class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s = '#'.join(s)
        s = '$#'+s+'#^'
        p = [0 for i in range(len(s))]
        id, mx = 0, 0
        left, max_len = 0, 1
        for i in range(1, len(s)-1):
            if mx - i > 0:
                p[i] = min(p[id *2 - i], mx - i)
            l = i - p[i] - 1
            r = i + p[i] + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                p[i] += 1
                l -= 1
                r += 1
            if max_len < p[i]:
                max_len = p[i]
                left = l+1
            if mx < r - 1:
                id = i
                mx = r - 1
        return filter(lambda x: x != '#' and x != '$' and x != '^', s[left:left+max_len*2+1])

solution = Solution()
print solution.longestPalindrome('aa')
