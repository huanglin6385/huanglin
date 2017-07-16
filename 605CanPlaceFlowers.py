#87.54
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        length = len(flowerbed)
        flowerbed.append(0)
        left = 0
        while left<length and flowerbed[left] == 0:
            if flowerbed[left+1] == 0:
                left += 2
                n -= 1
                if n==0:
                    return True
            else:
                break
        while left < length:
            if flowerbed[left] == 1:
                left += 1
                continue
            else:
                while left+1 < length and flowerbed[left] == 0 and flowerbed[left + 1] == 0 and flowerbed[left+2] == 0:
                    left += 2
                    n-=1
                    if n==0:
                        return True
                left += 1


        return  n==0