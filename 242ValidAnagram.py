#91.29
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = sorted(nums[:3])[::-1]
        m = sorted(nums[:3])[:2]
        for i in nums[3:]:
            if i <= m[0]:
                m[1], m[0] = m[0], i
            elif i < m[1]:
                m[1] = i

            if i >= result[0]:
                result[0], result[1], result[2] = i, result[0], result[1]
            elif i >= result[1]:
                result[1], result[2] = i, result[1]
            elif i >= result[2]:
                result[2] = i

        return max(result[0] * result[1] * result[2], result[0] * m[0] * m[1])
