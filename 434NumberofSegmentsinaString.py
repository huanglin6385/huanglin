#71.79
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        sign = False
        for i in range(len(s)):
            if s[i] != " ":
                sign = True
            else:
                if sign:
                    result += 1
                sign = False

        return result + int(sign)