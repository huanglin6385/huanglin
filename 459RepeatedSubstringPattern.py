#15
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        long = 1
        while long <= length / 2:

            while s[long] != s[0]:
                long += 1

            if length % long != 0:
                continue
            else:
                sign = True
                for i in range(1, length / long):
                    for j in range(long):
                        if s[j] != s[j + long * i]:
                            sign = False
                            break
                    if sign == False:
                        break
                if sign:
                    return True

        return False

#80.16
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s*2)[1:-1]