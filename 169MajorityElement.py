#46.42
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = collections.defaultdict(int)
        length = len(nums)
        for i in nums:
            dict1[i] += 1
            if dict1[i] > length/2:
                return i
