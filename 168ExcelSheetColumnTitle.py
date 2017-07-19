#92.76
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""

        while n:
            result += chr((n-1)%26 + 65 )
            n = (n-1)/26
        return result[::-1]


test = Solution()
print test.convertToTitle(28)