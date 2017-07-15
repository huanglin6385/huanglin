#96.42
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == [] or k == 0:
            return False
        k += 1
        window = set(nums[:k])
        if len(window) < len(nums[:k]):
            return True
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            if nums[i] in window:
                return True
            window.add(nums[i])

        return False