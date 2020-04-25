t = int(input())
while t:
    n = int(input())
    n = n*2
    arr = list(map(int, input().split()))
    pairs = []
    while len(arr):
        pair = [arr.pop(0), arr.pop(0)]
        pairs.append((tuple(pair)))
    pairs.sort(key=lambda x: x[0])
    print(pairs)
    chain = [pairs.pop(0)]
    while True:
        try:
            if pairs[0][0] > chain[-1][1]:
                chain.append(pairs.pop(0))
            else:
                pairs.pop(0)
        except:
            break
    # print(chain)
    print(len(chain))
    t -= 1