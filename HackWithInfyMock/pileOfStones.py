'''
There is a pile of N stones. A and B decided to play a game.
In one chance, a player can choose either 1 stone or even number of stones,
i.e., 1 or 2, 4, 6, 8, 10, 12,......

If the player is unable to pick up a stone, then he/she loses. meaning,if they have no stones to pick from.
Player 'A' always starts first.

Example:
    N = 30, A wins, because he picks them all as 30 is even
    N = 3, no matter what, A loses because, if he chooses 1, B takes 2 and A loses
                                            if he chooses 2, B takes 1 and A loses
    N = 4, A wins, because he picks them all as 4 is even



Solution:
    In pile problems, you'll have to keep in mind that both the players play optimally, (usually specified)
    So, you'll have to think of a base case that both the players will try to bring the game down to
    which guarantees them a win.

    The base case in this scenario is bringing the number of stones in the pile to 3 in such a way that
    the opposite player will have to choose from the 3 stones.

    In the case of 3 stones, as discussed earlier, the person who has to pick from 3 stones, loses
    no matter what.
    This gives A the advantage of being able to choose first.

    If N == 1 or N == even, because A chooses first, he will optimally pick them all,
    leaving B with nothing to pick from, thereby being the winner.

    If N == 3, which is the base case, because A has to choose, he will be the loser

    If N != 3 and N == odd, as A will want to win and play optimally, he will try to bring the game down
    to remaining N as 3. For any given odd N, other than 3, he can bring it down to 3.

    i.e., If N == 17, A chooses 14, leaving 3 for B to choose from, B loses
    N == 69, A chooses 66, leaving 3 for B to choose from, B loses

    So, the only scenario, A loses is when N == 3 to begin with.
'''

tc = int(input())


def ans():
    n = int(input())
    if n == 3:
        return 'B'
    else:
        return 'A'


for _ in range(tc):
    print(ans())

