#41.77
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"

        stack = range(1, n + 1)
        result = ""
        z = 1
        for i in stack:
            z *= i
        z /= n
        n -= 1
        while k:
            result += str(stack[(k - 1) / z])
            del stack[(k - 1) / z]
            k %= z

            z /= n
            n -= 1

        for i in xrange(len(stack) - 1, -1, -1):
            result += str(stack[i])

        return result



