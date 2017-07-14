#83.77
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_number = min(0, nums[0])
        result = max(nums)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            result = max(result, nums[i] - min_number)
            min_number = min(min_number, nums[i])

        return result