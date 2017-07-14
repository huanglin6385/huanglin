#88.30
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        history_0 = 0
        history_1 = nums[0]
        for i in range(1, len(nums)):
            history_0,history_1 = max(history_0,history_1),nums[i] + history_0

        return max(history_0,history_1)