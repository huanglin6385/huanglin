#93.07
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sign = 0
        number = 0
        for string in s:
            if string == 'L':
                if sign == 2:
                    return False
                sign += 1
            elif string == "A":
                number += 1
                sign = 0
                if number > 1:
                    return False
            else:
                sign = 0

        return True