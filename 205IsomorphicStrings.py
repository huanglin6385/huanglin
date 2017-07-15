#80.11
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] in dict1:
                if t[i] not in dict2:
                    return False
                if dict1[s[i]] != dict2[t[i]]:
                    return False
            else:
                if t[i] in dict2:
                    return False

                dict1[s[i]] = i
                dict2[t[i]] = i

        return True