#87.27
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        result = set([1])
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                result.add(i)
                result.add(num/i)

        if sum(result) == num:
            return True
        return False