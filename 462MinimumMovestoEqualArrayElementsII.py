#81.55
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = sorted(nums)[len(nums)/2]
        return sum([abs(i-k) for i in nums])