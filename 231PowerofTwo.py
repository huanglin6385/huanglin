#76.87
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if str(bin(n)).count("1") == 1:
            return True
        return False
