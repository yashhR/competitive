def ways():
    n = int(input())
    count = 0
    for i in range(-n, n+1):
        if i*i<n:
            for j in range(i, n+1):
                if i*i+j*j == n:
                    count += 12
                elif i*i+j*j<n:
                    for k in range(j, n+1):
                        if i*i+j*j+k*k == n:
                            count += 24
                        elif i*i+j*j+k*k < n:
                            for l in range(k, n+1):
                                if i*i+j*j+k*k+l*l == n:
                                    count += 24
                                else:
                                    continue
    print(count)
t=int(input())
for i in range(t):
    ways()
