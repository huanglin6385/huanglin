#81.12
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        for i in range(1,num+1):
            result[i] = result[i/2] + i%2

        return result