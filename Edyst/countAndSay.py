
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

print(countAndSay(5))
