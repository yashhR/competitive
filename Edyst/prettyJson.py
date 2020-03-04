s = '["foo", {"bar":["baz",null,1.0,2]}]'
'''
{
    "A":"B",
    "C":
    {
        "D":"E",
        "F":
        {
            "G":"H",
            "I":"J"
        }
    }
}
'''
strings = []
indents = 0
temp = ''
for i in range(len(s)):
    if s[i] == '{' or s[i] == '[':
        if temp != '':
            strings.append("    "*indents + temp)
        temp = ''
        strings.append("    "*indents + s[i])
        indents += 1
    elif s[i] == '}' or s[i] == ']':
        if temp != '':
            strings.append("    " * indents + temp)
        temp = ''
        indents -= 1
        strings.append("    "*indents + s[i])
    elif s[i] == ',':
        if temp != '':
            strings.append("    "*indents + temp + ',')
        temp = ''
    else:
        if s[i] != " ":
            temp = temp + s[i]

for i in strings:
    print(i)
