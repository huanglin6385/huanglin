#38.53
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        length = len(p)
        dict2 = collections.Counter(p)
        dict1 = collections.Counter(s[:length])
        if dict1 == dict2:
            result.append(0)
        for i in range(length, len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict1[s[i - length]] -= 1
            if dict1[s[i - length]] == 0:
                del dict1[s[i - length]]

            if dict1 == dict2:
                result.append(i - length + 1)

        return result