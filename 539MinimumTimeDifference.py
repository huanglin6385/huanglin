#56.53
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = []
        for time in timePoints:
            hour, minute = time.split(":")
            times.append(int(hour) * 60 + int(minute))

        times.sort()
        times.append(times[0] + 24 * 60)
        ans = 0x7FFFFFFF
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i - 1])

        return ans