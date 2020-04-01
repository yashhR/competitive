# from collections import Counter
T = int(input())
for _ in range(T):
    c1 = {}
    c2 = {}
    s = input()
    n = len(s)
    if n % 2 == 0:
        # c1 = Counter(s[:n//2])
        # c2 = Counter(s[n//2:])
        for i in range(n//2):
            if s[i] not in c1:
                c1[s[i]] = 1
            else:
                c1[s[i]] += 1

        for i in range(n//2, n):
            if s[i] not in c2:
                c2[s[i]] = 1
            else:
                c2[s[i]] += 1
        if c1 == c2:
            print("YES")
        else:
            print("NO")
    else:
        # c1 = Counter(s[:n//2])
        # c2 = Counter(s[n//2 + 1:])
        for i in range(n // 2):
            if s[i] not in c1:
                c1[s[i]] = 1
            else:
                c1[s[i]] += 1

        for i in range(n // 2 + 1, n):
            if s[i] not in c2:
                c2[s[i]] = 1
            else:
                c2[s[i]] += 1
        if c1 == c2:
            print("YES")
        else:
            print("NO")


# dict1 = {1: 10, 2: 5, 'a': 17, 'b': 69}
#
# dict2 = {2: 5, 'a': 17, 'b': 69, 1: 10}
#
# print(dict1 == dict2)

'''
6
gaga
abcde
rotor
xyzxy
abbaab
ababc
'''
