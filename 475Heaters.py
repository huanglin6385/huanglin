import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        result = max(heaters[0] - houses[0], houses[-1] - heaters[-1], 0)
        p = set(heaters)
        for i in range(1, len(heaters)):
            distance = (heaters[i] - heaters[i - 1]) / 2
            if heaters[i - 1] + distance in p and heaters[i] - distance in p:
                result = max(result, distance)
            else:
                d1 = bisect.bisect(houses, heaters[i - 1] + distance)
                d2 = bisect.bisect(houses, heaters[i] - distance)

                if d1 != 0 and d2 != len(houses):
                    result = max(houses[d1 - 1] - heaters[i - 1], heaters[i] - houses[d2], result)
                elif d1 == 0 and d2 == len(houses):
                    continue
                elif d1 == 0:
                    result = max(heaters[i] - houses[d2], result)
                elif d2 == len(houses):
                    result = max(houses[d1 - 1] - heaters[i - 1], result)

        return result

