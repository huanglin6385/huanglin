#77.91
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = set([])

        def backtracking(left, right, path):
            if left < 0 or right < 0 or left > right:
                return
            elif left == right == 0:
                res.add(path)

            backtracking(left - 1, right, path + "(")
            backtracking(left, right - 1, path + ")")

        backtracking(n, n, "")
        return list(res)