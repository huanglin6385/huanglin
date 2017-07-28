#19.73
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        result = 0

        for i in range(32):
            count_1 = 0
            for index in range(length):
                if nums[index]&1 == 1:
                    count_1 += 1
                nums[index]<<=1
            result += count_1 * (length - count_1)

        return result


