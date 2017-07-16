#38.13
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<=1
            result += n%2
            n/=2
            if n == 0:
                result <<=(32-i-1)

        return result