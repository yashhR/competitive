'''
Mack gives Daisy two strings S1 and S2-consisting only of characters-
'M' and 'D' , and asks her to convert S1 to S2 in exactly N moves.

In a single move, Daisy has two choices:

Exchange any one 'M' with a 'D', or
Exchange any one 'D' with a 'M'.
You need to help Daisy if it's possible to transform S1 to S2 in exactly N moves. Output "Yes" if possible, else "No".


Input Format:
First line contains T, the number of test cases. T lines follow.
Each line consists of 2 space separated strings S1 and S2, and and the value N.


Output Format:
For each test case, print the answer, either "Yes" or "No"-(Without the quotes).


Constraints:
1 ≤ T ≤ 250
1 ≤ |S1|=|S2| ≤ 50
1 ≤ N ≤ 100

SAMPLE INPUT
3
MMDMDDM DDDDDDD 2
MMDD MMDD 1
MMMMMDMM DDDDDMDD 8
SAMPLE OUTPUT
No
No
Yes
'''

'''
We know that if two strings are the same, then any even number of changes will work, because we can just keep changing
the same character again and again and after even number of switches, we will get back the same string again


That is our base case and we are going to build our solution off of that.


So, let's just write that case:
'''

s1, s2, n = input().split()
n = int(n)

if s1 == s2 and n % 2 == 0:
    print("Yes")
elif s1 == s2 and n % 2 != 0:    # Can't get the same string from same string in odd number of switches
    print("No")


'''
The minimum number of moves we need to make the strings the same is the number of characters that are not the same
in both the strings, we will need atleast those number of moves to switch each one of them
So, lets count the number of characters that arent the same in the respective positions
'''
count = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1

'''
We now have the count of the different characters between s1 and s2
This is the bare minimum that we need.
In these number of moves, we can make the strings equal, but the given number may be higher,
again we are back to our base case, that the strings are equal and we still have moves to make!
that's right! -- if that remaining number of moves is even, then yes, we can do it, else nope bro, fuck it!
'''

if n == count and (n-count)%2 == 0:
    print("Yes")
else:
    print("No")
