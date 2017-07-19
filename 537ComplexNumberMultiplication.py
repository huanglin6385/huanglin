#89.29
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        number_1 = a.rstrip("i").split("+")
        number_2 = b.rstrip("i").split("+")
        number_1[0] = int(number_1[0])
        number_1[1] = int(number_1[1])
        number_2[0] = int(number_2[0])
        number_2[1] = int(number_2[1])

        return str(number_1[0] * number_2[0] - number_1[1] * number_2[1]) + "+" + str(
            number_1[1] * number_2[0] + number_1[0] * number_2[1]) + "i"