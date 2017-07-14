#99.85
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = set(["a","e","i","o","u","A","E","I","O","U"])
        left = 0
        right = len(s)-1
        s = list(s)
        while left<right:
            if s[left] in p:
                if s[right] in p:
                    s[left],s[right] = s[right],s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            elif s[right] in p:
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(s)
