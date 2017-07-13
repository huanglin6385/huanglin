#67.92
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return [1,2][n-1]
        result = [1,2]
        for i in range(2,n):
            result.append(result[-1]+result[-2])

        return result[-1]