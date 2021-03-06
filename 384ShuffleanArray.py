#11.24
import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self.histroy = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.histroy

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self._nums)
        return self._nums



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()