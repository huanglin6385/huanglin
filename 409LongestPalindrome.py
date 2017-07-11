#79.83
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dict1 = collections.Counter(s)
        for val in dict1.values():
            result += val / 2 * 2
        for val in dict1.values():
            if val%2 == 1:
                return result+1
        return result
