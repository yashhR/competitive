# from collections import Counter
#
#
# def group_anagrams(strs):
#     haha = {}
#     returnlist = []
#     for string in strs:
#         c = Counter(string)
#         bitch = tuple(sorted(c.items()))
#         if bitch in haha:
#             haha[bitch].append(string)
#         else:
#             haha[bitch] = [string]
#     for item in haha.items():
#         returnlist.append(item[1])
#     return returnlist
#
#
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# This solution beats 6.73% of all python solutions, so FUCK this!


# def group_anagrams(strs):
#     returnlist = []
#     haha = {}
#     for string in strs:
#         freq = {}
#         for c in string:
#             if c in freq:
#                 freq[c] += 1
#             else:
#                 freq[c] = 1
#         freq = sorted(freq.items())
#         if f"{freq}" in haha:
#             haha[f"{freq}"].append(string)
#         else:
#             haha[f"{freq}"] = [string]
#     for item in haha.items():
#         returnlist.append(item[1])
#     return returnlist
#
#
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def group_anagrams(strs):
    words = {}
    for string in strs:
        key = ''.join(sorted(string))
        if key in words:
            words[key].append(string)
        else:
            words[key] = [string]
    return list(words.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# This does better than 95.71% of all python solutions
