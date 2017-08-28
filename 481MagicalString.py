#75,14
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [1, 2, 2]
        index = 2
        while len(stack) < n:
            stack += stack[index] * [3 - stack[-1]]
            index += 1

        return stack[:n].count(1)