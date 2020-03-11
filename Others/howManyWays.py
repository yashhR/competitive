'''
num_ways(3) -> c (1 way)
num_ways(12) -> 1, 2 or 12 -> ab or l (2 ways)
num_ways(143) -> 1, 4, 3 or 14, 3 -> adc or nc (3 ways)
num_ways(122) -> 1, 2, 2 or 12, 2 or 1, 22 -> abb or lb or av


Why not use recursion
'''


s = input()


def num_ways(som):
    count = 0
    if len(som) == 1 and int(som) != 0:
        return 1
    elif len(som) == 2:
        if som[0] == '0':
            return 0
        elif 27 > int(som) > 0:
            count += 1
            for i in som:
                count += num_ways(i)
            return count

print(num_ways(s))


