#80.39
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left < right:
            mid = (left + right) / 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid-1
            else:
                left = mid+1

        return left**2==num or right**2==num
