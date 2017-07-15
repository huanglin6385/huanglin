#74.09
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        now = 9
        k = 1
        while n>now:
            now += 9 * 10**k *(k+1)
            k += 1

        now -= 9 * 10**(k-1) *k
        return int(str(10**(k-1) + (n-1-now)/k)[(n-1-now)%k])
