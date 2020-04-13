'''
Little Syed loves brute force. He thinks that brute force can be the solution to any problem in the world.
You give him any question, and he'll have a brute force answer ready for you, almost all the time.
His good friend Little Jhool (Like, always!) decides to teach him a lesson,
by giving him problems which cannot be solved by brute force, because he wants Syed to learn algorithms.

Given a number, n, Syed needs to find the number closest to n, though less than n which satisfies Jhoolsswingingtheorem.
Jhool's swinging Theorem: A number n, such that it can be expressed as a sum of two positive algebraic cubes;
 AND, if that number can be expressed in such a manner in more than one way - it satisfies the theorem.

Now, everyone here on HackerEarth knows how much we hate Little Jhool (No, not really!) -
so we want you to help Syed in figuring out Jhool's queries - once and for all!

Input Format:
The first line contains an integer, t - denoting the number of test cases.

The next t lines will contain, an integer - n - denoting the number which Jhool gives.

Output Format:
You have to print the previous number satisfying the given constraints. If no such previous number exists, print -1.

Constraints:
1 <= t <= 100
1 <= n <= 704977

SAMPLE INPUT
2
100
4150
SAMPLE OUTPUT
-1
4104
Explanation
In the first case, since no such number below 100 exists, the result is -1.
In the second case, 4104 is the answer because:
(4096 + 8 = 4104) or (161616 + 222) and (3375 + 729 = 4104) or (151515 + 999) -
that is, there is more than one way in which 4104 can be expressed, satisfying the theorem.
'''

'''
I can only think of brute-force, even that I am hesitant to implement.

For the example test case, we know that the maximum we could go is - 4^3, because 5^3 is 125 and we are only
allowed to sum up two POSITIVE algebraic cubes, so 4 is the upper limit. 

The closest to 100, so we would obviously have to compute the sum of cubes of numbers at the end of range (1, 2, 3,4)

If we do 4^3 + 4^3 = 128, that's more than 100
How about 4^3 + 3^3 = 64 + 9 = 73 - 73 can be expressed as a sum of two algebraic cubes, but that's just one way
Can we find another pair of numbers whose cubes add up to 73, apparently not. We need to make pairs out of 
1, 2, 3, 4 and see if any of those pairs cubes add up to 73, thereby 73 having more than a way of being expressed.


----
 
I think the way to getting started with this is first by getting the upper bound, 
so let's do that
'''

from itertools import combinations

n = 4150
number = 1
while number**3 < n:
    number += 1

print(f"upperbound is {number - 1}, it's cube is {(number - 1)**3}")


lols = list(combinations(range(1, number), r=2))

for i in range(len(lols)):
    lols[i] = list(lols[i])

possibles = {}
ret = 0
for each in lols:
    num = each[0]**3 + each[1]**3
    if num < n:
        if num in possibles:
            possibles[num] += 1
            ret = max(ret, num)
        else:
            possibles[num] = 1

print(ret)

'''
Lol, guess what! I knew it works but I didn't think the hackerearth judge would accept it because its just
brute-force and possibly uses up more memory and time than thats allocated.

I submitted the code 1 minute before the timer and it got accepted.
'''