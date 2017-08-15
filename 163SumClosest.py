#57
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                p = nums[i] + nums[left] + nums[right]
                if p == target:
                    return p

                if abs(p - target) < abs(ans - target):
                    ans = p

                if p - target < 0:
                    left += 1
                else:
                    right -= 1

        return ans





