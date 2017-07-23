#91.94
import collections
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dict1 = collections.defaultdict(int)
        for w in wall:
            r = 0
            for number in w[:-1]:
                r+=number
                dict1[r]+=1

        return len(wall)-max(dict1.values() or [0])