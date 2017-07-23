#84.61
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*len(len(word2)) for _ in range(len(word1))]



        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    if i>0 and j>0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i>0 and j>0:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]


        return dp[-1][-1]