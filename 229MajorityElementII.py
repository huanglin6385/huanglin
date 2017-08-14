#33.20
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return list(set(nums))
        number1, number2, count1, count2 = nums[0], nums[0], 0, 0
        for i in range(len(nums)):
            if nums[i] == number1:
                count1 += 1
            elif nums[i] == number2:
                count2 += 1
            else:
                if count1 != 0 and count2 != 0:
                    count1 -= 1
                    count2 -= 1
                else:
                    if count1 == 0:
                        number1 = nums[i]
                        count1 = 1

                    if count2 == 0:
                        number2 = nums[i]
                        count2 = 1

        dict1 = {}
        dict1[number1] = 0
        dict1[number2] = 0
        result = []
        for i in range(len(nums)):
            if nums[i] == number1:
                dict1[number1] += 1
            elif nums[i] == number2:
                dict1[number2] += 1
        if dict1[number1] > len(nums) / 3:
            result.append(number1)

        if dict1[number2] > len(nums) / 3:
            result.append(number2)
        return list(set(result))
