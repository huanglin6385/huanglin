#86.98
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = n%10
        n /= 10
        result = []
        sign = False
        while n:
            remainder = n%10
            n /= 10
            if remainder < right:
                result.append(right)
                result.append(remainder)
                sign = True
                break
            result.append(right)
            right = remainder




        if not sign:
            return -1

        result.sort(reverse = True)
        for i in range(len(result)-1,-1,-1):
            if result[i] > remainder:
                n = n*10 + result[i]
                del result[i]
                break
        p = n*10**len(result)+sum([result[i]*10**i for i in range(len(result))])
        if p>0x7FFFFFFF:
            return -1
        return p