values = list(map(int, input().split()))
lost = []
ans = []
def sumOfDigits(num):
    res = 0
    while(num!=0):
        div = num % 10
        res = res + div
        num = num//10
    return res


for i in range(len(values)):
    lost.append(sumOfDigits(values[i]))

for i in range(len(lost)):
    for j in range(0, len(lost)-i-1):
        if lost[j] > lost[j+1]:
            (lost[j], lost[j+1]) = (lost[j+1], lost[j])
            (values[j], values[j+1]) = (values[j+1], values[j])
        elif lost[j] == lost[j+1]:
            if values[j] > values[j+1]:
                (values[j+1], values[j]) = (values[j], values[j+1])

print(values)




