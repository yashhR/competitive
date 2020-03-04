days = int(input())
prevCellState = list(map(int, input().split()))

def cellCompare(prev):
    cellState = []
    for i in range(8):
        if i == 0:
            if prev[1] == 0:
                cellState.append(0)
            else:
                cellState.append(1)
        elif i == 7:
            if prev[6] == 0:
                cellState.append(0)
            else:
                cellState.append(1)
        elif prev[i-1] == prev[i+1]:
            cellState.append(0)
        else:
            cellState.append(1)
    return cellState

bro = prevCellState
#bro1 = cellCompare(bro)

for i in range(days):
    bro = cellCompare(bro)

print(bro)
