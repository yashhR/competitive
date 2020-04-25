# t = int(input())
# while t:
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     if k == 1:
#         print("yes")
#     else:
#         while True:
#             swaps = 0
#             for i in range(n):
#                 for j in range(i+k, n):
#                     if arr[i] > arr[j]:
#                         arr[i], arr[j] = arr[j], arr[i]
#                         swaps += 1
#             if swaps == 0:
#                 break
#         if arr == sorted(arr):
#             print("yes")
#         else:
#             print("no")
#     t -= 1


t = int(input())
while t:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == 1:
        print("yes")
    else:
        og = sorted(arr)
        ref = {}
        for i in range(n):
            if og[i] in ref:
                ref[og[i]].append(i)
            else:
                ref[og[i]] = [i]
        found = False
        for i in range(n):
            if len(ref[arr[i]]) == 1:
                idx = ref[arr[i]][0]
                if abs(idx - i) % k != 0:
                    found = True
                    print("no")
                    break
            else:
                okay = False
                for idx in ref[arr[i]]:
                    if abs(idx - i) % k == 0:
                        # print(arr[i], i, idx)
                        okay = True
                        break
                if not okay:
                    found = True
                    print("no")
                    break
        if not found:
            print("yes")
    t -= 1