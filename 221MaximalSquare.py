#93.73
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        res = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        p = 0
        for i in range(len(matrix)):
            res[i][0] = int(matrix[i][0])
            if res[i][0] == 1:
                p = 1

        for j in range(len(matrix[0])):
            res[0][j] = int(matrix[0][j])
            if res[0][j] == 1:
                p = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    res[i][j] = min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1]) + 1
                    p = max(p, res[i][j])

        return p * p
