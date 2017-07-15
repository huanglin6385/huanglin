#80.30
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        p = set(["[", "{", "("])
        dict1 = {"]": "[", "}": "{", ")": "("}
        stack = []
        for i in s:
            if i in p:
                stack.append(i)
            else:
                if stack == []:
                    return False
                head = stack.pop()
                if dict1[i] != head:
                    return False

        if stack == []:
            return True
        return False

