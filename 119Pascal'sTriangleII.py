#92.18
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        result = [1]
        number = 1
        for i in range(1, rowIndex):
            number = number * (rowIndex - i) / i
            result.append(number)

        return result




