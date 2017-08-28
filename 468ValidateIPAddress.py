#16.18
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        IP = IP.lower()
        if IP.find(".") != -1:
            IP = IP.split(".")
            if len(IP) != 4:
                return "Neither"
            for i in IP:
                if i == "" or i.startswith("0"):
                    if i == "0":
                        continue
                    return "Neither"
                else:
                    for j in i:
                        if j < "0" or j > "9":
                            return "Neither"
                    if int(i) > 255:
                        return "Neither"
            return "IPv4"

        else:
            IP = IP.split(":")
            if len(IP) != 8:
                return "Neither"
            for i in IP:
                if len(i) > 4 or len(i) < 1:
                    return "Neither"
                else:
                    for j in i:
                        if "0" <= j <= "9" or "a" <= j <="f":
                            continue
                        return "Neither"
            return "IPv6"