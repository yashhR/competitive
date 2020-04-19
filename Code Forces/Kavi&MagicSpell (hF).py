'''
Kaavi has a string T of length m and all the strings with the prefix T are magic spells.
Kaavi also has a string S of length n and an empty string A.

During the divination, Kaavi needs to perform a sequence of operations. There are two different operations:

Delete the first character of S and add it at the front of A.
Delete the first character of S and add it at the back of A.
Kaavi can perform no more than n operations.
To finish the divination, she wants to know the number of different operation sequences to make A a magic spell
(i.e. with the prefix T).
As her assistant, can you help her? The answer might be huge, so Kaavi only needs to know the answer modulo 998244353.

Two operation sequences are considered different if they are different in length or there exists an i that their i-th operation is different.

A substring is a contiguous sequence of characters within a string. A prefix of a string S is a substring of S that occurs at the beginning of S.

Input
The first line contains a string S of length n (1≤n≤3000).

The second line contains a string T of length m (1≤m≤n).

Both strings contain only lowercase Latin letters.

Output
The output contains only one integer  — the answer modulo 998244353.

Examples
inputCopy
abab
ba
outputCopy
12
inputCopy
defineintlonglong
signedmain
outputCopy
0
inputCopy
rotator
rotator
outputCopy
4
inputCopy
cacdcdbbbb
bdcaccdbbb
outputCopy
24
'''

s = input()
s = list(s)
t = input()
t = list(t)
n = len(s)
m = len(t)
A = [s[0]]
answer = 0
idx = 1
memo = {}


def operation(s, A, T, n, m, idx):
    global answer
    print(''.join(A))
    if len(A) >= m:
        if A[:m] == T:
          answer += 1
    # print(answer)
    if len(A) == n:
        return None
    else:
        x = s[idx]
        idx += 1
        proxy1 = []
        proxy1[:] = A
        proxy1.insert(0, x)
        proxy2 = []
        proxy2[:] = A
        proxy2.append(x)
        operation(s, proxy1, T, n, m, idx)
        operation(s, proxy2, T, n, m, idx)


operation(s, A, t, n, m, idx)
print(2*answer)
