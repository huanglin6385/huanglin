#54
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        if n <= 4:
            return [1,2,4][n-2]
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5,n+1):
            dp[i] = max([dp[j]*dp[i-j] for j in range(2,i-2)]+[i])

        return dp[-1]

