#72.73
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(" ")
        result = 0
        for i in s[::-1]:
            if i == " ":
                return result
            else:
                result += 1

        return result