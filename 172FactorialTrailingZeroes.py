#88.59
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 5
        result = 0
        while k <= n:
            result += n / k
            k *= 5

        return result