#87.49
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        counter = 0
        for i in range(len(nums)):
            if nums[i] == res:
                counter += 1
            elif counter > 0:
                counter -= 1
            else:
                res = nums[i]
                counter = 1

        return res