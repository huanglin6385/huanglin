#65.26
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0

        result = 0
        q = A[1] - A[0]
        number = 2
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == q:
                number += 1
            else:
                if number >= 3 :
                    result += (number - 2) * (number - 1) / 2
                number = 2
                q = A[i] - A[i - 1]
        if number >= 1:
            return result+(number - 2) * (number - 1) / 2
        return result
