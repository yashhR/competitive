'''
A sophomore Computer Science student is frustrated with boring college lectures.
Professor X agreed to give him some questions; if the student answers all questions correctly,
then minimum attendance criteria will not apply to him.

Professor X chooses a sequence A1,A2,…,AN and asks Q queries.
In each query, the student is given an integer P; he has to construct a sequence B1,B2,…,BN,
where P⊕Ai=Bi for each valid i (⊕ denotes bitwise XOR),
and then he has to find the number of elements of this sequence which have an even number of 1-s in the binary
representation and the number of elements with an odd number of 1-s in the binary representation.
Help him answer the queries.

Input:

The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains two space-separated integers N and Q.
The second line contains N space-separated integers A1,A2,…,AN.
Q lines follow. Each of these lines contains a single integer P describing a query.

Output:

For each query, print a single line containing two space-separated integers ―
the number of elements with an even number of 1-s and
the number of elements with an odd number of 1-s in the binary representation.

Constraints:
1≤T≤100
1≤N,Q≤105
T⋅(N+Q)≤4⋅106
1≤Ai≤108 for each valid i
1≤P≤105
The input/output is quite large, please use fast reading and writing methods.

Subtasks
Subtask #1 (30 points): N,Q≤1,000
Subtask #2 (70 points): original constraints

Example Input:
1
6 1
4 2 15 9 8 8
3

Example Output:
2 4

Explanation:
Example case 1: The elements of the sequence B are P⊕4=7, P⊕2=1, P⊕15=12, P⊕9=10, P⊕8=11 and P⊕8=11.
The elements which have an even number of 1-s in the binary representation are 12 and 10,
while the elements with an odd number of 1-s are 7, 1, 11 and 11.
'''

t = int(input())


def ans():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    while q:
        p = int(input())
        a = [p ^ f for f in a]
        q -= 1
    count = 0
    for i in range(len(a)):
        if len([x for x in bin(a[i]) if x == '1']) % 2 == 0:
            count += 1
    print(count, n-count)


for i in range(t):
    ans()