#72.67
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        judge = set([])
        for i in nums:
            if i in judge:
                return False
            judge.add(i)
        return True
