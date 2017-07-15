#96.88
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0]

        for string in strs[1:]:
            if string.startswith(result):
                continue
            else:
                if result.startswith(string):
                    result = string
                    continue
                right = 0
                while string[right] == result[right]:
                    right += 1
                right -= 1
                result = result[:right]
                if result == "":
                    return ""

        return result