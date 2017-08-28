#47.25
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in range(3,len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
        for i in range(4,len(x)):
            if x[i] + x[i-4] >= x[i-2] and x[i-1] == x[i-3]:
                return True
        for i in range(5,len(x)):
            if x[i-2] >= x[i-4] and x[i-1] <= x[i-3] and x[i] + x[i-4] >= x[i-2] and  x[i-1] + x[i-5] >= x[i-3]:
                return True
        return False