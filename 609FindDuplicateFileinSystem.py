#86.76
import collections
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dict1 = collections.defaultdict(list)
        for string in paths:
            now = string.split(" ")
            for txt in now[1:]:
                r = txt.rstrip(")").split("(")
                dict1[r[1]].append(now[0] + "/" + r[0])
        result = []
        for i in dict1:
            if len(dict1[i]) > 1:
                result.append(dict1[i])

        return result