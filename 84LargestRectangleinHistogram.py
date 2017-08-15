#75.60
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for left in range(len(heights)):
            while heights[left] < heights[stack[-1]]:
                h = heights[stack.pop()]
                ans = max(ans, (left - stack[-1] - 1) * h)

            stack.append(left)
        return ans




test = Solution()
print test.largestRectangleArea([1,1,1.1,1.1,1.1,1.2])