#72.65
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        history = 0
        lena = len(a)
        lenb = len(b)
        if lena < lenb:
            a = "0" * (lenb - lena) + a
        else:
            b = "0" * (lena - lenb) + b

        result = ""
        for i in xrange(max(lena, lenb) - 1, -1, -1):
            number = int(a[i]) + int(b[i]) + history
            result += str(number % 2)
            history = number / 2

        if history == 1:
            return "1" + result[::-1]
        return result[::-1]