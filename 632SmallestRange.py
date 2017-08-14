#78.87
import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        stack = [(nums[i][0],i,0)for i in range(len(nums))]
        heapq.heapify(stack)
        right = max(row[0] for row in nums)
        ans = [0x7FFFFFFF,None,None]

        while stack:
            now_min,min_row,row_index = heapq.heappop(stack)
            if right - now_min < ans[0]:
                ans[0]  = right - now_min
                ans[1] = now_min
                ans[2] = right

            if row_index + 1 >= len(nums[min_row]):
                return ans[1:]
            right = max(right,nums[min_row][row_index+1])
            heapq.heappush(stack, (nums[min_row][row_index+1],min_row,row_index+1))

        return ans[1:]