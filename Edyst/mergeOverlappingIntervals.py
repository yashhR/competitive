arr = [[1, 3], [2, 5], [6, 9]]
def merge(ar):
    # since given set is ordered we consider the start and end of the scale
    scaleend = ar[-1][1]
    scalestart = ar[0][0]
    scale = []
    result = []
    for i in range(scalestart, scaleend+1):
        scale.append(0)
    for i in ar:
        for j in range(i[0]-1, i[1]):
            scale[j] = 1
    print(scale)
    def getIntervals(ar):
        starts = [1]
        ends = []
        for i in range(len(ar) - 1):
            if ar[i] == 0 and ar[i + 1] == 1:
                starts.append(i + 2)
            elif ar[i] == 1 and ar[i + 1] == 0:
                ends.append(i + 1)
        ends.append(len(ar))
        result = []
        for i in range(len(starts)):
            result.append([starts[i], ends[i]])
        return result
    print(getIntervals(scale))

merge(arr)
def getIntervals(onesAndzeros):
    starts = [1]
    ends = []
    for i in range(len(onesAndzeros)-1):
        if onesAndzeros[i] == 0 and onesAndzeros[i+1] == 1:
            starts.append(i+2)
        elif onesAndzeros[i] == 1 and onesAndzeros[i+1] == 0:
            ends.append(i+1)
    ends.append(len(onesAndzeros))

    result = []

    for i in range(len(starts)):
        result.append([starts[i], ends[i]])
    return result




