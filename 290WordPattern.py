#77.76
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(pattern)):
            if pattern[i] in dict1:
                if str[i] not in dict2:
                    return False
                if dict1[pattern[i]] != dict2[str[i]]:
                    return False
            else:
                if str[i] in dict2:
                    return False

                dict1[pattern[i]] = i
                dict2[str[i]] = i

        return True


