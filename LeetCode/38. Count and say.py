# def countAndSay(n):
#     sequence = ['1', '11', '21', '1211']
#     def next(bro):
#         prev = bro
#         distincts = [prev[0]]
#         counts = []
#         count = 1
#         for i in range(1, len(prev)):
#             if i == len(prev) - 1:
#                 if prev[i] == distincts[-1]:
#                     count += 1
#                     counts.append(count)
#                 else:
#                     counts.append(count)
#                     distincts.append(prev[i])
#                     counts.append(1)
#             if prev[i] == distincts[-1]:
#                 count += 1
#             else:
#                 counts.append(count)
#                 count = 1
#                 distincts.append(prev[i])
#         ans = ''
#         for i in range(len(counts)):
#             ans += str(counts[i]) + distincts[i]
#         sequence.append(ans)
#     if n < 5:
#         return int(sequence[n-1])
#     else:
#         while len(sequence) != n:
#             next(sequence[-1])
#         print(sequence)
#         return int(sequence[n-1])


# Faster than 10.40% of all Python submissions
# print(countAndSay(7))


def count_and_say(n):
    sequence = ['1', '11', '21', '1211']

    def new_add(prev):
        next = ''
        i = 0
        count = 1
        while i < len(prev) - 1:
            bitch = prev[i]
            if i == len(prev) - 2:
                if bitch != prev[i+1]:
                    next += str(count) + bitch
                    next += '1' + prev[i+1]
                else:
                    count += 1
                    next += str(count) + bitch
            else:
                if prev[i+1] == bitch:
                    count += 1
                else:
                    next += str(count) + bitch
                    count = 1
            i += 1
        sequence.append(next)
    if n < 5:
        return sequence[n-1]
    else:
        while len(sequence) != n:
            new_add(sequence[-1])
        # print(sequence)
        return sequence[n-1]


# Faster than 37.50% of all python solutions
print(count_and_say(7))
