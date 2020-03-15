'''

def countAndSay(n):
    sequence = [1, 11, 21, 1211]
    def add_next():
        last = str(sequence[-1])
        distincts = [last[0]]
        counts = []
        count = 1
        for i in range(1, len(last)):
            if i == len(last) - 1:
                if last[i] == distincts[-1]:
                    count += 1
                    counts.append(count)
                else:
                    counts.append(count)
                    distincts.append(last[i])
                    counts.append(1)
            else:
                if last[i] == distincts[-1]:
                    count += 1
                else:
                    distincts.append(last[i])
                    counts.append(count)
                    count = 1
        val = ''
        for i in range(len(counts)):
            val += f"{counts[i]}{distincts[i]}"
        return val
    if n < 5:
        return sequence[n-1]
    else:
        while len(sequence) <= n:
            x = add_next()
            sequence.append(x)
        return sequence[n-1]

print(countAndSay(9))
'''


def cas(x):
    res = ['1', '11', '21', '1211']

    def ans(re):
        prev = re[-1]
        counts = []
        distincts = [prev[0]]
        count = 1
        for i in range(1, len(prev)):
            if i == len(prev) - 1:
                if prev[i] == distincts[-1]:
                    count += 1
                    counts.append(count)
                else:
                    counts.append(count)
                    distincts.append(prev[i])
                    counts.append(1)
            else:
                if prev[i] == distincts[-1]:
                    count += 1
                else:
                    distincts.append(prev[i])
                    counts.append(count)
                    count = 1
        resu = ''
        for i in range(len(counts)):
            resu += str(counts[i])
            resu += str(distincts[i])
        return resu
    if x < 5:
        return res[x-1]
    else:
        while len(res) <= x:
            res.append(ans(res))
        print(res)
        return res[-1]


print(cas(5))