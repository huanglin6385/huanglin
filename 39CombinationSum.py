#61.18
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(target, candidates, path, start):
            if target < 0:
                return
            elif target == 0:
                result.append(path)
                return

            for index in range(start, len(candidates)):
                backtracking(target - candidates[index], candidates, path + [candidates[index]], index)

        candidates.sort()
        backtracking(target, candidates, [], 0)

        return result
