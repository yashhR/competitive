'''
Input:
2
6 2
1 1 1 2 2 1
5 3
1 1 2 2 1
Example Output
3
5
'''
from collections import Counter
t = int(input())

def longest_sub():
    n, k = map(int, input().split())
    flavours = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(n-1, 0, -1):
            c = Counter(flavours[i:j+1])
            if len(c) < k:
                return len(flavours[i:j+1])

for i in range(t):
    print(longest_sub())
