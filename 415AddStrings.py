#62.68
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        history = 0
        result = ""
        length1 = len(num1)
        length2 = len(num2)
        if length1 < length2:
            num1 = "0"*(length2-length1)
        else:
            num2 = "0"*(length1-length2)
        for i in xrange(max(length1,length2)-1,-1,-1):
            n1 = int(num1[i])
            n2 = int(num2[i])
            result += str((n1 + n2 + history)%10)
            history = (n1 + n2 + history)/10
        if history == 1:
            result += "1"
        return result[::-1]