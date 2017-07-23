#63.93
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        p = 1
        for i in range(1,len(nums))
            p*=nums[i-1]
            result[i] = p

        p = 1
        for i in xrange(len(nums)-2,-1,-1):
            p*=nums[i+1]
            result[i] *=p

        return result