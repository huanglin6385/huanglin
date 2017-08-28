#78.93
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in xrange(31,-1,-1):
            prefix = {num>>i for num in nums}

            ans <<= 1
            ans += 1
            sign = False
            for pre in prefix:
                if pre ^ ans in prefix:
                    sign = True
                    break

            if not sign:
                ans -= 1
        return ans
