t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    # yo = list(set(arr))
    # yo.sort()
    # j = 0
    # c = 0
    # m = 0
    # i = 0
    # while c != len(yo):
    #     curr = arr[i % n]
    #     # print(curr, yo[j])
    #     if i % n == 0:
    #         m += 1
    #     if curr == yo[j]:
    #         c += 1
    #         j += 1
    #     i += 1
    # print(m)
    last_occ = {}
    first_occ = {}
    hehe = []
    k = 0
    for i in range(n):
        if arr[i] in last_occ:
            last_occ[arr[i]] = i
        else:
            first_occ[arr[i]] = i
            last_occ[arr[i]] = i
            hehe.append(arr[i])
            k += 1
    # print(last_occ)
    hehe.sort()
    j = 0
    c = 0
    m = 1
    while c < k and j < k-1:
        print(f"We are at {hehe[j]} it's fc is {first_occ[hehe[j]]}, looking for {hehe[j+1]}, its last occ is {last_occ[hehe[j+1]]}")
        if last_occ[hehe[j+1]] < first_occ[hehe[j]]:
            m += 1
        # else:
        #     first_occ[hehe[j+1]] = last_occ[hehe[j+1]]
        j += 1
        c += 1
    print(m)
    t -= 1