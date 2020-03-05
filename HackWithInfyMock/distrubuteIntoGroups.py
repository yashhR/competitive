a = [1, 2, 3, 4, 5]
n = len(a)
m = 4

maxes = []

if m == 2:
    for i in range(n-1):
        maxes.append(max(sum(a[:i+1]), sum(a[i+1:])))
elif m == 3:
    for i in range(n-m+1):
        for j in range(i+1, n-1):
            maxes.append(max(sum(a[:i+1]), sum(a[i+1:j+1]), sum(a[j+1:])))
elif m == 4:
    for i in range(n-m+1):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                maxes.append(max(sum(a[:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:])))
elif m == 5:
    for i in range(n-m+1):
        for j in range(i+1, n-3):
            for k in range(j+1, n-2):
                for l in range(k+1, n-1):
                    maxes.append(max(sum(a[:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:l+1]), sum(a[l+1:])))

print(min(maxes))


