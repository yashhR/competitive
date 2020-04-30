def backtract(s, res, i):
    if i == len(s) -1:
        print(res)
        return
    else:
        if s[i] == '?':
            backtract(s, res + '0', i+1)
            backtract(s, res + '1', i+1)
        else:
            backtract(s, res + s[i], i + 1)


backtract("1??0", "", 0)