# t = int(input())
# while t:
#     n = int(input())
#     poses = list(map(int, input().split()))
#     infected = 1
#     hehe = set(poses)
#     # neighbors = {}
#     lol = []
#     for pos in poses:
#         count = 0
#         # neighbors[pos] = 0
#         if pos + 1 in hehe:
#             # neighbors[pos] += 1
#             count += 1
#         if pos + 2 in hehe:
#             # neighbors[pos] += 1
#             count += 1
#         if pos - 1 in hehe:
#             # neighbors[pos] += 1
#             count += 1
#         if pos - 2 in hehe:
#             # neighbors[pos] += 1
#             count += 1
#         lol.append((pos, count))
#     # print(lol)
#     lol.sort(key=lambda x: x[1])
#     print(lol[0][1] + 1, lol[-1][1] + 1)
#     t -= 1


t = int(input())
while t:
    n = int(input())
    positions = list(map(int, input().split()))
    bc = []
    i = 0
    while i < n:
        idx = i
        c = 1
        while idx + 1 < n and positions[idx+1] - positions[idx] <= 2:
            c += 1
            idx += 1
        bc.append((i, c))
        i = idx + 1
    if len(bc) == 1:
        print(bc[-1][-1], bc[-1][-1])
    else:
        bc.sort(key=lambda x: x[1])
        print(bc[0][1], bc[-1][-1])
    t -= 1