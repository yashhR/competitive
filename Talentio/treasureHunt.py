'''
Explore the array for the treasure
values in the array are clues
each cell has int b/w 11 and 55
for each value, tens digit represents the row and ones digit represents the column in which the next clue is there
Treasure is the cell who's value is same as the coordinates

Program should output the cells it visits during its search, and a message indicating where you found the treasure

Input:
34 21 32 41 25
14 42 43 14 31
54 45 52 42 23
33 52 51 31 35
21 52 33 13 23
'''
A=[[34,21,32,41,25],[14,42,43,14,31],[54,45,52,42,23],[33,15,51,31,35],[21,52,33,13,23]]
l=[]
n=A[0][0]
i1=0
j1=0
def treasureHunt(n) :
    num=n
    j=num%10
    num=num//10
    i=num%10
    l.append(n)
    if i1==(i-1) and j1==(j-1) :
        for i in range(len(l)) :
            print(l[i],end=" ")
    else :
        i1=i
        j1=j
        n=A[i-1][j-1]
        treasureHunt(n)
treasureHunt(n)




