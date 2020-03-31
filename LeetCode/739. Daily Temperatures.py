'''
739. Daily Temperatures (Medium)

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''


# def daily_temperatures(T):
#     return_list = []
#     new_maxi = max(T)
#     for i in range(len(T)):
#         if i == len(T) - 1:
#             return_list.append(0)
#         else:
#             if T[i] == new_maxi:
#                 T[i] = -1
#                 new_maxi = max(T[i:])
#                 return_list.append(0)
#             else:
#                 for j in range(i+1, len(T)):
#                     if T[j] > T[i]:
#                         return_list.append(j-i)
#                         break
#     return return_list


def daily_temperatures(T):
    return_list = []
    bitches = {}
    for i in range(len(T)):
        if T[i] in bitches:
            bitches[T[i]] += 1
        else:
            bitches[T[i]] = 1
    for i in range(len(T)-1):
        print(i)
        maxi = max(bitches)
        if T[i] == maxi:
            bitches[maxi] -= 1
            return_list.append(0)
            if bitches[maxi] == 0:
                del bitches[maxi]
        else:
            for j in range(i+1, len(T)):
                flag = 0
                if T[j] > T[i]:
                    flag = 1
                    return_list.append(j-i)
                    break
            if not flag:
                return_list.append(0)
    return_list.append(0)
    return return_list


print(daily_temperatures([100,65,67,52,63,40,92,44,66,39]))

