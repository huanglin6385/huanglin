#70.91
import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = collections.Counter(nums)
        result = 0
        for i in dict1:
            if dict1.has_key(i+1):
                result = max(dict1[i] + dict1[i + 1], result)

        return result