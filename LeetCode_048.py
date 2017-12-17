class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return [[]]
        res = zip(*matrix)
        res = [[i for i in r[::-1]] for r in res]
        for i in range(len(matrix)):
            matrix[i] = res[i]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
solution.rotate(matrix)
print matrix
