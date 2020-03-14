'''
s = "RRRULULDLD"
'''

s = "RRRULULDLD"

opposite = {
            "L": "R",
            "U": "D"
            }

opposite.update({v: k for k, v in opposite.items()})

sides = ['R', 'L']
ups_downs = ['U', 'D']


width = 0
height = 0
now = s[0]    # prev = R
subtract = 0
for i in range(1, len(s)):
    if s[i] == now:
        if now in sides:
            width += 1
        else:
            height += 1
    elif s[i] != now:
        try:
            if s[i] == prev:
                subtract += width*height
        except NameError:
            pass
        prev = s[i-1]
        now = s[i]

print((s.count("R")*s.count("U")) - subtract)



'''          ___________
         |      _____|
         |    |
 _______ |    |
|_____________|'''
'''

'''