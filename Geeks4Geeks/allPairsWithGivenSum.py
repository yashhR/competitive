t = int(input())
while t:
    n, m, x = map(int, input().split())
    result = []
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    setOf2 = set()
    for num in arr2:
        setOf2.add(num)
    for num in arr1:
        if x - num in setOf2:
            result.append((num, x-num))
    result.sort(key= lambda x: x[0])
    if len(result) > 0:
        for i in range(len(result)):
            if i == len(result) - 1:
                print(result[i][0], result[i][1])
            else:
                print(result[i][0], result[i][1], end=", ")
    else:
        print(-1)
    t -= 1

'''
Main optimization point:
using a set() so that the lookup become O(1) and hence making the tc as O(n) + O(n) rather than O(n^2   )
'''

'''
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1
'''