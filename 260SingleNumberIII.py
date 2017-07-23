#90.20
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            k = k^i
        number = 1
        while k&1==0:
            k>>=1
            number<<=1
        r1 = 0
        r2 = 0
        for i in nums:
            if i&number == 0:
                r1 ^= i
            else:
                r2 ^= i
        return [r1,r2]