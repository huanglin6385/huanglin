#63.47
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        p = int(math.log(n,3)+0.00000001)
        if 3**p == n:
            return True
        return False
