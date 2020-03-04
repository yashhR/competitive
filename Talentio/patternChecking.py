#string = input()

dict = {'{':'}', '(':')', '[':']', '<':'>'}
print(dict.keys())
'''for i in dict_keys(['(','[']):
    print(i)'''
'''commentStart = "@*"
commentEnd = "*@"
for i in range(len(string)):
    if string[i:i+2] == commentStart:
        for j in range(len(string[i+2:])):
            if string[i+2+j:i+j+4] == commentEnd:
                string[i:j+2] = '''''


'''for i in range(len(string)):
    if string[i] in dict.keys():
        flag = 0
        for j in string[i+1:]:
            if j == dict[string[i]]:
                flag = 1
                string.replace(j, ' ')
                break

if flag:
    print(True)
else:
    print(False)

'''
# ({a%(d(@*(((*@dd)do;;)[][][}[)]
