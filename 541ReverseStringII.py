#71.43
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        left = 0
        while left < len(s):
            result += s[left:left+k][::-1]
            result += s[left+k:left+2*k]
            left += 2*k

        return result
