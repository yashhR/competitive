'''
weights = [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]
weights.sort(reverse=True)
ability = 3.00
totalTrips = 0
for i in range(len(weights)):
    if weights[i] > ability:
        weights.remove(weights[i])
while len(weights) != 0:
    total = 0
    eachTrip = []
    for i in range(len(weights)):
        if total + weights[i] <= ability:
            eachTrip.append(weights[i])
            total += weights[i]
    print(eachTrip)
    for i in range(len(eachTrip)):
        weights.remove(eachTrip[i])
    totalTrips += 1
print(totalTrips)
'''

ability = 3.00
weights = list(map(float, input().split()))
weights.sort(reverse=True)
total = 0

while len(weights) > 0:
    eachTrip = []
    lol = 0
    for i in range(len(weights)):
        if lol + weights[i] <= ability:
            eachTrip.append(weights[i])
            lol += weights[i]
    print(eachTrip)
    for i in range(len(eachTrip)):
        weights.remove(eachTrip[i])
    total += 1

print(total)
