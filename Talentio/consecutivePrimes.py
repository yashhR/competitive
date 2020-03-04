lines = int(input())

lost = []
li = []
for i in range(lines):
    lost.append(int(input()))
    li.append([])

def isPrime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 1

for y in lost:
    for i in range(0, y+1):
        if isPrime(i):
            li[index(y)]

 def noOfPrimes(someRange):
     pcount = 0
     for i in range(3,someRange+1):
         x = 1
         if sum(li[li.index(someRange)]):


