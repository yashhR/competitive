def firstUniqChar(self, s: str) -> int:
    # uniques = []
    # seen = set()
    # for c in s:
    #     if c not in seen:
    #         uniques.append(c)
    #         seen.add(c)
    #     else:
    #         try:
    #             uniques.remove(c)
    #         except:
    #             pass
    # if len(uniques):
    #     return s.index(uniques[0])
    # return -1
    lol = {}
    for i in range(len(s)):
        if s[i] in lol:
            lol[s[i]] = (lol[s[i]][0] + 1, i)
        else:
            lol[s[i]] = (1, i)
    for i in range(len(s)):
        if lol[s[i]][0] == 1:
            return lol[s[i]][1]
    return -1