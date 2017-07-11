#91.09
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        result = length*(1+length)/2
        for i in nums:
            result -= i

        return result