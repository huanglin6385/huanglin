#47.84
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append([0] * (i + 1))
            result[i][0] = 1
            result[i][-1] = 1
            for j in range(1, i):
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1]

        return result
