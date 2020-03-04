def bitch(l1, s):
    randi = []
    for i in range(len(l1)):
        for j in range(i+1, len(l1)+1):
            if sum(l1[i:j]) == s:
                randi.append([i+1, j])
    maxi = 0
    bruh = None
    for i in randi:
        if i[1]-i[0]>maxi:
            maxi = i[1]-i[0]
            bruh = i
    return bruh
print(bitch([1,2,3,4,5,0,0,0,6,7,8,9,10], 15))



