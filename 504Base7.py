#59.33
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return "-" + self.base(num*(-1))
        elif num > 0:
            return self.base(num)
        else:
            return "0"
    def base(self,num):
        result = ""
        while num != 0:
            result = str(num%7) + result
            num /= 7

        return result