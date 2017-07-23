#51.10
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        dict1 = collections.Counter(s)
        dict2 = collections.defaultdict(list)
        for key in dict1:
            dict2[dict1[key]].append(key)
        nums = sorted(dict2.keys())
        for i in nums[::-1]:
            result += "".join([i*t for t in dict2[i]])

        return result