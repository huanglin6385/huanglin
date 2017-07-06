#33.96
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min([s.find(key) for key,val in collections.Counter(s).iteritems() if val == 1] or [-1])