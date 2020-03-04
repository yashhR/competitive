dirs = {"NORTH": "N",
        "SOUTH": "S",
        "WEST": "W",
        "EAST": "E",
        "North": "N",
        "South": "S",
        "West": "W",
        "East": "E"}
def dirReduc(arr):
    def get_key(val):
        for key, vals in dirs.items():
            if val == vals:
                return key
    for i in range(len(arr)):
        arr[i] = dirs[arr[i]]
    s = ' '.join(arr)
    print(s)
    if "N S" in s or "S N" in s or "E W" in s or "W E" in s:
        s = s.replace("N S", "")
        s = s.replace("S N", "")
        s = s.replace("E W", "")
        s = s.replace("W E", "")
        s = s.replace(" ", "")
        bro = []
        for i in s:
            bro.append(get_key(i))
        return dirReduc(bro)
    else:
        res = []
        for i in range(len(s)):
            if s[i] != " ":
                res.append(get_key(s[i]))
    return res

print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))

