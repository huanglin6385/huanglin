#81.7
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        history = 1
        for i in xrange(len(digits)-1,-1,-1):
            now = history + digits[i]
            if now<10:
                digits[i] = now
                return digits
            digits[i] = 0

        return [1] + digits

