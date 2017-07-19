#37.98
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        result = 0
        while x:
            result += x%10
            x /= 10
            result *= 10
        result *= sign
        if result<-2147483648 or result >2147483647:
            return 0
        return result
