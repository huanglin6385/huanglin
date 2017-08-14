#52.02
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_A_B = {}
        sum_C_D = {}
        for i in A:
            for j in B:
                sum_A_B[i+j] = sum_A_B.get(i + j,0) + 1

        for i in C:
            for j in D:
                sum_C_D[i + j] = sum_C_D.get(i + j, 0) + 1

        result = 0
        for i in sum_A_B:
            if -i in sum_C_D:
                result += sum_A_B[i]*sum_C_D[-i]

        return result
