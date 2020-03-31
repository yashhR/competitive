# T = int(input())
#
# def solve():
#     prev = input()
#     if len(prev) == 1:
#         return "NO"
#     if len(set(prev)) == 1 and len(prev) == 2:
#         return "NO"
#     if len(set(prev)) == 1 and len(prev) > 2:
#         return "YES"
#     counts = []
#     distincts = [prev[0]]
#     count = 1
#     for i in range(1, len(prev)):
#         if i == len(prev) - 1:
#             if prev[i] == distincts[-1]:
#                 count += 1
#                 counts.append(count)
#             else:
#                 counts.append(count)
#                 distincts.append(prev[i])
#                 counts.append(1)
#         else:
#             if prev[i] == distincts[-1]:
#                 count += 1
#             else:
#                 distincts.append(prev[i])
#                 counts.append(count)
#                 count = 1
#     resu = ''
#     for i in range(len(counts)):
#         resu += str(distincts[i])
#         resu += str(counts[i])
#     if len(resu) < len(prev):
#         return "YES"
#     return "NO"
#
# for _ in range(T):
#     print(solve())
#
# '''
# 3
# bbbbbbbbbbaa
# c
# aaaaaaaaaabcdefgh
#

T = int(input())


def solve():
    n = int(input())
    gE = list(map(int, input().split()))
    def is_perfect(some):
        yes = False
        for i in range(len(some)-1):
            if some[i] == some[i+1] - 1:
                yes = True
            else:
                return False
        if yes:
            return True
        return False
    haha = is_perfect(gE)
    if n == 1:
        print(f"{gE[0]}")
    elif n == 2:
        print(f"{gE[0]},{gE[1]}")
    elif n == 3:
        for i in range(len(gE)-1):
            if gE[i] == gE[i+1] - 1:
                flag = 1
            else:
                flag = 0
                print(f"{gE[0]},{gE[1]},{gE[2]}")
                break
        if flag:
            print(f"{gE[0]}...{gE[-1]}")
    elif haha:
        print(f"{gE[0]}...{gE[-1]}")
    else:
        return_list = []
        idx = 0
        while idx < len(gE) - 1:
            start = gE[idx]
            if idx == len(gE) - 2:
                return_list.append(f"{start}")
                idx += 1
            else:
                count = 1
                for i in range(idx, len(gE)-1):
                    if i == len(gE) - 1:
                        count += 1
                    else:
                        if gE[i + 1] == gE[i] + 1:
                            count += 1
                        else:
                            last = gE[i]
                            break
                if count > 2:
                    return_list.append(f"{start}...{last}")
                    idx += count
                else:
                    return_list.append(f"{start}")
                    idx += 1
        return_list.append(gE[-1])
        for i in range(len(return_list)):
            if i == len(return_list) - 1:
                print(f"{return_list[i]}")
            else:
                print(f"{return_list[i]}", end=",")


for _ in range(T):
    solve()

'''
3
12
1 2 3 5 6 8 9 10 11 12 15 17
4
4 5 7 8
1
4
'''