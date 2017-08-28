#30.23
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        number = range(1, 10)
        result = []

        def backtracking(stack, path, target, deepth):
            if deepth <= 0 or target <= 0:
                if deepth == 0 and target == 0:
                    result.append(path)
                return

            for index in range(len(stack)):
                backtracking(stack[index + 1:], path + [stack[index]], target - stack[index], deepth - 1)

        backtracking(number, [], n, k)
        return result