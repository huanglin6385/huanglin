#85.97
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False]*len(nums)
        left = 0
        r = 0
        while left < len(nums):
            history_left = left
            now_max = 0
            while left < len(nums) and not visited[left]:
                now_max+=1
                visited[left] = True
                left = nums[left]
            r = max(r,now_max)
            left = history_left+1
            while left<len(nums) and visited[left]:
                left+=1
        return r