#84.95
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        result = duration
        now_max = timeSeries[0] + duration
        for i in range(1,len(timeSeries)):
            if timeSeries[i]<now_max:
                result = result - now_max + timeSeries[i] + duration
            else:
                result += duration
            now_max = timeSeries[i] + duration

        return result