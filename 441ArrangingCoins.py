import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = int(math.sqrt(2 * n))
        while (number + 1) * (number + 2) / 2 > n:
            number -= 1

        return number + 1