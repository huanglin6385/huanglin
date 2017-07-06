#68.4
import collections
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = sorted(nums,reverse=True)
        r = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        dict1 = collections.defaultdict(list)
        for i in range(len(ranks)):
            dict1[ranks[i]].append(i + 1)
        result = []
        for i in nums:
            rank = dict1[i].pop()
            if rank <= 3:
                result.append(r[rank])
            else:
                result.append(str(rank))

        return result