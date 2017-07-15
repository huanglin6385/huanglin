#76.06
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int((c / 2) ** 0.5) + 1):
            b = int((c - i ** 2) ** 0.5)
            if i ** 2 + b ** 2 == c:
                return True

        return False