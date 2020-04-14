from collections import Counter

w = input().lower()
count = Counter(w)


def is_ana(test):
    for c, v in count.items():
        if c not in test or v > test[c]:
            return False
    return True


n = int(input())
total = 0
for i in range(n):
    x = input().lower()
    total += int(is_ana(Counter(x)))
print(total)