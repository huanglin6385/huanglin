#88.69
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 :
            return False
        p = int(math.log(num,4))
        if 4**p == num:
            return True
        return False
