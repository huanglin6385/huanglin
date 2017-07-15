#82.21
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        while left < n:
            mid = (left + n) / 2
            p = guess(mid)
            if p == 1:
                left = mid + 1
            elif p == -1:
                n = mid - 1
            else:
                return mid
        if guess(left) == 0:
            return left
        return n
