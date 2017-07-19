#47.79
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1

        return result
