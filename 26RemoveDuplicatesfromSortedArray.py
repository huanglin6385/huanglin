#74.99
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        left = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[left] = nums[i]
                left += 1

        return left