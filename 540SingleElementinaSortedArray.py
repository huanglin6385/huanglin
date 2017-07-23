#58.18
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        while left<len(nums):
            if nums[left]!= nums[left-1]:
                return nums[left-1]
            left += 2
        return nums[-1]