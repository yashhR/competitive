import itertools
def get_pins(observed):
    oList = [x for x in observed]
    adjacents = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'],
                 '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'], '8': ['0', '5', '7', '8','9'],
                 '9': ['6', '8', '9'], '0': ['0', '8']}
    possibles = []
    possibles.append(observed)
    lol = [adjacents[k] for k in observed]
    for i in range(len(oList)):
        lok = [p for p in itertools.product(*lol)]
        for j in lok:
            possibles.append(''.join(list(j)))
    return list(set(possibles))

print(get_pins('369'))
'''
import itertools
x = [1, 2, 3, 4, 5, 6]
[p for p in itertools.product(x, repeat=2)]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), 
 (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), 
 (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), 
 (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
'''