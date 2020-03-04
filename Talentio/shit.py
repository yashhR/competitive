input_string = input()
list_input = []
finalstr = ''
list_input = input_string.split(',')
for i in list_input:
    temp = i.split(':')
    name = temp[0]
    number = temp[1]
    length = len(name)
    max = 0

for digit in number:
    if(int(digit)<=length):
        if(max<int(digit)):
            max = int(digit)
    if(max==0):
        finalstr += 'X'
    else:
        finalstr+=name[max-1]
print(finalstr)