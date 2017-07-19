#92.59
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return max(nums)
        one,two,three = sorted(nums[:3])
        for number in nums[3:]:
            if number <= one:
                continue
            elif number <= two:
                one = number
            elif number <= three:
                two,ont = three,two
            elif number >three:
                three ,two , one = number, three,two

        return one