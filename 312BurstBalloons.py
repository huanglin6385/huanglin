#62.55
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]

        for distance in range(2,len(nums)):
            for i in range(len(nums)-distance):
                for k in range(i+1,i+distance):
                    dp[i][i+distance] = max(dp[i][k] + dp[k][i+distance]+nums[i]*nums[k]*nums[i+distance], dp[i][i+distance])
        return dp[0][-1]



zz = Solution()
print zz.maxCoins([3,1,5,8])