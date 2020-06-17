class Solution:
    def is_hex(s):
        hex_digits = set("0123456789abcdefABCDEF")
        for char in s:
            if not (char in hex_digits):
                return False
        return True
    def validIPAddress(self, IP: str) -> str:
        dots = False
        colons = False
        for c in IP:
            if c == ".":
                dots = True
                break
            elif c == ":":
                colons = True
                break
        if dots:
            after_split = IP.split(".")
            invalid = False
            if len(after_split) != 4:
                return "Neither"
            for each in after_split:
                try:
                    if not each.isnumeric():
                        return "Neither"
                    if len(each) < 1:
                        invalid = True
                        break
                    if each[0] == "0" and len(each) > 1:
                        invalid = True
                        break
                    if int(each) > 255 or int(each) < 0:
                        invalid = True
                        break
                except ValueError:
                    return "Neither"
            if invalid:
                return "Neither"
            else:
                return "IPv4"
        if colons:
            invalid = False
            after_split = IP.split(":")
            if len(after_split) != 8:
                return "Neither"
            for each in after_split:
                if not Solution.is_hex(each):
                    return "Neither"
                if len(each) > 4:
                    invalid = True
                    break
                elif len(each) < 1:
                    invalid = True
                    break
            if invalid:
                return "Neither"
            else:
                return "IPv6"
        return "Neither"
                
            
            
                