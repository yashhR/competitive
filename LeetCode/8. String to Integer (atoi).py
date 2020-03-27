class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        if str[0].isnumeric() or str[0]=='+':
            if str[0] == "+":
                if len(str) == 1:
                    return 0
                if str[1].isnumeric():
                    ret = ''
                    for c in str[1:]:
                        if c.isnumeric():
                            ret += c
                        else:
                            break
                    result = int(ret)
                    if 2**31 - 1 >= result >= -2**31:
                        return result
                    else:
                        return 2**31 - 1
                else:
                    return 0
            ret = ''
            for c in str:
                if c.isnumeric():
                    ret += c
                else:
                    break
            result = int(ret)
            if 2**31 - 1 >= result >= -2**31:
                return result
            else:
                return 2**31 - 1
        elif str[0] == '-':
            ret = ''
            if len(str) == 1:
                return 0
            if str[1].isnumeric():
                for c in str[1:]:
                    if c.isnumeric():
                        ret += c
                    else:
                        break
                result = int(ret)
                if 2**31 - 1 >= result >= -2**31:
                    return -result
                else:
                    return -2**31
            else:
                return 0
        return 0