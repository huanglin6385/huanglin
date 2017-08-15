#17
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sss = nums[left] + nums[right] + nums[i]
                if sss == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > 0 and nums[right] == nums[right + 1]:
                        right -= 1
                    continue

                if sss < 0:
                    left += 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while nums[right] == nums[right + 1]:
                        right -= 1

        return ans

