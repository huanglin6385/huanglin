#70.95
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        right = len(nums) - 1
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] >= nums[right]:
                right = i
                continue
            break

        if right == 0:
            nums[:] = nums[::-1]
            return

        ll = None
        for k in range(i + 1, len(nums)):
            if nums[k] > nums[i]:
                if ll == None:
                    ll =  k
                elif  nums[ll] > nums[k]:
                    ll = k

        nums[ll], nums[i] = nums[i], nums[ll]
        nums[i + 1:] = sorted(nums[i + 1:])