mod = 998244353
t = int(input())


def f(some):
    print(some)
    maxi = max(arr)
    aux = [0 for x in range(n + 1)]
    for num in arr:
        aux[num] = -1
    for i in range(1, len(aux)):
        if aux[i] == 0:
            return i
    return maxi + 1


def print_subsequences(arr, index, subarr):
    global ans
    if index == len(arr):
        if len(subarr) != 0:
            ans += f(subarr)
    else:
        print_subsequences(arr, index + 1, subarr)
        print_subsequences(arr, index + 1, subarr + [arr[index]])
    return


while t:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    print_subsequences(arr, 0, [])
    print(ans + 1)
    t -= 1