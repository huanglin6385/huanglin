#17.73
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left_min = 0x7FFFFFFFF
        stack = []
        for x in nums:
            while stack and stack[-1][1] <= x:
                stack.pop()

            if stack and x > stack[-1][0]:
                return True

            left_min = min(left_min,x)
            stack.append([left_min,x])

        return False





zz = Solution()
print zz.find132pattern([3,5,3,0,4])