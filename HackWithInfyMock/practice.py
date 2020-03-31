from itertools import permutations

noOfDigits = int(input())
givenSet = list(input().split())
k = int(input())

perm = permutations(givenSet, k)

lol = [int(''.join(each)) for each in perm if each[0] != '0']

lol.sort()

for i in range(len(lol)):
    if lol[i] % 3 == 0:

        print(lol[i])
        break
