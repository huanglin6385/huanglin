#86.30
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 5:
            return ["1", "11", "21", "1211"][n - 1]
        result = ""
        count = 1
        result_n_1 = self.countAndSay(n - 1)
        string = result_n_1[0]
        for i in range(1, len(result_n_1)):
            if result_n_1[i] == string:
                count += 1
            else:
                result += str(count) + str(string)
                count = 1
                string = result_n_1[i]

        if count > 0:
            return result + str(count) + str(string)
        return result
