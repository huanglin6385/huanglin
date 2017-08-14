#76.31
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        result = [[]for _ in range(len(matrix[0])+len(matrix)-1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if (i+j) %2 == 0:
                #     result[i+j].insert(0,matrix[i][j])
                # else:
                result[i+j].append(matrix[i][j])

        out = []
        for i in range(len(result)):
            if i%2 == 0:
                out.extend(result[i][::-1])
            else:
                out.extend(result[i])
        return out

