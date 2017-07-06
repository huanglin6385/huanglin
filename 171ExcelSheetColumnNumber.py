#86.67
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((ord(string) - 64)*(26**index) for index,string in enumerate(s[::-1]))