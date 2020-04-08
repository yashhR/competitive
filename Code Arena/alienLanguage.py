'''
Alice got a message M. It is in an alien language.
A string in an alien language is said to be valid if it contains the letter a or z.
Alice decided to count the number of valid substrings of the message M. Help him to do this.
Two substrings are different if it occurs at different positions in the message.

Input:
First line of the input contains the number of test cases T. It is followed by T lines. Each line has a single string M.


Output:
For each test case, output a single number, the number of valid substrings.


Constraints:
|M| <= 10^6
M contains only lower case latin latters, that is characters a to z.

Read the editorial here.

SAMPLE INPUT
4
abcd
azazaz
abbzbba
flkjdh
SAMPLE OUTPUT
4
21
22
0

'''

t = int(input())
for _ in range(t):
    m = input()


    def count_sub_str(m, n, x, y):
        res = 0
        count = 0
        for i in range(n):
            if m[i] == x or m[i] == y:
                res += ((count + 1) * (n - i))
                count = 0
            else:
                count += 1
        return res


    a = count_sub_str(m, len(m), 'a', 'z')
    print(a)