'''
for a given array, to find the maximum sum of the contiguous sub array, we:
consider the best we could do at one element of the array, and for the next element we decide between itself or
whether to add the previous sum or not
'''


def maxTill(idx, ar):
    if idx == 0:
        return ar[idx]
    else:
        if idx in dict.keys():
            return dict[idx]
        else:
            return max(ar[idx] + maxTill(idx - 1, ar), ar[idx])


arr = [-5, -10, -20, -35, -34, -2, -11]
dict = {}
max_arr = []

for i in range(len(arr)):
    max_arr.append(maxTill(i, arr))
    dict[i] = maxTill(i, arr)

print(max(max_arr))