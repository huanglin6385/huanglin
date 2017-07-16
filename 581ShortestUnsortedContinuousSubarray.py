#90.72
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = sorted(nums)
        if result == nums:
            return 0
        left = 0
        while left < len(nums) and nums[left] == result[left]:
            left += 1
        right = len(nums) - 1
        while nums[right] == result[right]:
            right -= 1
        return right -left + 1