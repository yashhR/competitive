'''def sort_by_name(arr):
    dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
            18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
            70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred", 300: "three hundred",
            400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred",
            900: "nine hundred", 1000: "one thousand", 2000: "two thousand", 3000: "three thousand", 4000: "four thousand"
            , 5000: "five thousand", 6000: "six thousand", 7000: "seven thousand", 8000: "eight thousand", 9000: "nine thousand"}

    def get_key(val):
        for key, value in dict.items():
            if val == value:
                return key

    def to_name(val):
        if val in dict:
            return dict[val]
        else:
            s = ''
            k = len(str(val))
            l = len(str(val))
            if l == 1:
                s = dict[val]
            elif l == 2:
                if val in dict.keys():
                    s += dict[val]
                else:
                    for i in range(2):
                        if i == l - 1:
                            s += dict[int(str(val)[i])]
                        else:
                            s += dict[int(str(val)[i]) * 10] + "-"
            elif l == 3:
                for i in range(3):
                    if i == 2:
                        s += dict[int(str(val)[i])]
                    elif i == 1:
                        if int(str(val)[i:]) in dict.keys():
                            s += dict[int(str(val)[i:])]
                            break
                        else:
                            s += dict[int(str(val)[i])*10] + "-"
                    else:
                        s += dict[int(str(val)[i])] + " hundred "
            elif l == 4:
                for i in range(4):
                    if i == 3:
                        s += dict[int(str(val)[i])]
                    elif i == 2:
                        if int(str(val)[i:]) in dict.keys():
                            s += dict[int(str(val)[i:])]
                            break
                        else:
                            s += dict[int(str(val)[i])*10] + "-"
                    elif i == 1:
                        if val in dict.keys():
                            s += dict[val]
                            break
                        else:
                            s += dict[int(str(val)[i])] + " hundred "
                    else:
                        s += dict[int(str(val)[i])] + " thousand "


        return s

    words = []
    for i in arr:
        words.append(to_name(i))
        dict[i] = to_name(i)
    words.sort()
    res = []
    for i in words:
        res.append(get_key(i))

    return res'''
dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
            18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
            70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred", 300: "three hundred",
            400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred",
            900: "nine hundred", 1000: "one thousand", 2000: "two thousand", 3000: "three thousand", 4000: "four thousand"
            , 5000: "five thousand", 6000: "six thousand", 7000: "seven thousand", 8000: "eight thousand", 9000: "nine thousand"}


def to_name(val):
    if val in dict:
        return dict[val]
    else:
        s = ''
        k = len(str(val))
        l = len(str(val))
        if l == 1:
            s = dict[val]
        elif l == 2:
            if val in dict.keys():
                s += dict[val]
            else:
                for i in range(2):
                    if i == l - 1:
                        s += dict[int(str(val)[i])]
                    else:
                        s += dict[int(str(val)[i]) * 10] + "-"
        elif l == 3:
            for i in range(3):
                if i == 2:
                    s += dict[int(str(val)[i])]
                elif i == 1:
                    if int(str(val)[i:]) in dict.keys():
                        s += dict[int(str(val)[i:])]
                        break
                    else:
                        s += dict[int(str(val)[i]) * 10] + "-"
                else:
                    if dict[int(str(val)[i])] == "zero":
                        continue
                    else:
                        s += dict[int(str(val)[i])] + " hundred "
        elif l > 3:
            i = 0
            while i<l :
                if i == l-3:
                    if int(str(val)[i:]) in dict.keys():
                        s += dict[int(str(val)[i:])] + " "
                        break
                    else:
                        if dict[int(str(val)[i])] == "zero":
                            continue
                        else:
                            s += dict[int(str(val)[i])] + " hundred "
                    i += 1
                elif i == l-2:
                    if int(str(val)[i:]) in dict.keys():
                        s += dict[int(str(val)[i:])] + " "
                        break
                    else:
                        s += dict[int(str(val)[i]) * 10] + "-"
                    i += 1
                elif i == l-1:
                    if int(str(val)[i:]) in dict.keys():
                        s += dict[int(str(val)[i:])] + " "
                        break
                    else:
                        if dict[int(str(val)[i])] == "zero":
                            continue
                        else:
                            s += dict[int(str(val)[i])] + " hundred "
                    i += 1
                else:
                    s += to_name(int(str(val)[:-3])) + " thousand "
                    i += len(str(val)[:-3])

    return s

print(to_name(642994))