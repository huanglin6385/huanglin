#56.34
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return [1,9,91][n]
        elif n>=10:
            return 0
        result = 9
        k = 9
        n-=1
        while n:
            result*=k
            n-=1
            k-=1
        return result + self.countNumbersWithUniqueDigits(n-1)