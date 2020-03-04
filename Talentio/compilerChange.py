string = []
for i in range(3):
    string.append(input())
'''
for i in range(len(string)):
    for j in string[i]:
        if j == ';':
            string[i].replace(,'')
'''
for i in range(len(string)):
    string[i].replace('-', '.')
    string[i].replace('>', '')
for i in range(len(string)):
    print(string[i])
