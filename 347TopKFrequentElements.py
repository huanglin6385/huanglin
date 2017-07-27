#62.26
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict2 = collections.defaultdict(list)
        dict1 = collections.Counter(nums)
        for i in dict1:
            dict2[dict1[i]].append(i)
        if k >= len(dict1.keys()):
            return dict1.keys()
        o = sorted(dict2.keys())
        result = []
        for i in o[::-1]:
            if k > len(dict2[i]):
                result.extend(dict2[i])
                k -= len(dict2[i])
            else:
                return result + dict2[i][:k]

        return result