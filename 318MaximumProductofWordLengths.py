#99.66
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict1 = {}
        for i in words:
            mask = 0
            for j in set(i):
                mask |= 1<<(ord(j)-97)
            dict1[mask] = max(dict1.get(mask,0),len(i))

        return max([dict1[x]*dict1[y] for x in dict1 for y in dict1 if not x&y]+[0])