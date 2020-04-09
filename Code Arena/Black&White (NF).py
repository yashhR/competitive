'''
Problem:

Black and White are playing a game of chess on a chess board of n X n dimensions. The game is nearing its end. White has his King and a Pawn left. Black has only his King left. So, definitely Black cannot win the game. However, Black can drag the game towards a draw, and, he can do this only if he captures White's only left pawn. White knows exactly what he must do so that he wins the game. He is aware of the fact that if his Pawn reaches Row 'n' (topmost row as seen by White) , he is allowed to replace that Pawn by a Queen. Since White plays chess regularly, he knows how to beat the opponent in a situation in which the opponent has only a King left and he (White) has a King as well as a Queen left. The current scenario of the game will be given to you. You must tell whether this game will end with a Draw or will it end with White winning.

enter image description here

If Move = 0, it is currently White's move and if Move = 1, it is currently Black's move.

Black and White play alternately.

White's piece will be captured by Black if Black's King manages to reach the same square in which White's piece is currently in.

White's king is currently placed at the the point (1,n). White is in a hurry to convert his pawn into a queen, so , in every move of his, he only plays his pawn forward ( towards row n ), ignoring his king.

So, naturally, Black plays his King towards White's Pawn in order to capture it.

White's Pawn is currently located at the point (a,b).

Black's King is currently located at the point (c,d).

Pawn movement on a chess board : Pawn can move only one step forward, provided no piece is blocking it from doing so. ie. it can move only from (u,v) to (u+1,v), provided there is no piece (white or black) at (u+1,v)

King movement on a chess board : King can move one step in any direction. ie if it is at (u,v) currently, then it can move to (u+1,v) , (u-1,v) , (u,v+1) , (u,v-1) , (u+1,v+1) , (u+1, v-1) , (u-1,v+1) , (u-1,v-1), provided it remains inside the chess board

If at any moment the White Pawn is blocked by the black king from moving forward, white will be forced to play his king in such a case.

Input:

First line consists of T, the number of test cases. Every test case comprises of a single line containing space separated integers n, a, b, c, d, Move.

Output:

For every test case, print a single line, 'Draw' is the game ends as a draw or 'White Wins' if the game ends in white winning.

Constraints :

1<=T<=100000

5<=n<=10^9

2<=a<=n

1<=b,c,d<=n

0<=Move<=1

(c,d) != { (1,n) , (2,n) , (1,n-1) , (2,n-1) , (a,b) }

SAMPLE INPUT
2
10 6 2 10 2 0
10 5 2 1 3 0
SAMPLE OUTPUT
Draw
White Wins
Explanation
For first test case : white plays the first move since Move=0. white : Pawn moves from (6,2) to (7,2). black : King moves from (10,2) to (9,2). white : Pawn moves from (7,2) to (8,2). black : King moves from (9,2) to (8,2). white Pawn has been captured, so the game ends in a draw.

For second test case : white plays the first move since Move=0. white : Pawn moves from (5,2) to (6,2). black : King moves from (1,3) to (2,2). white : Pawn moves from (6,2) to (7,2). black : King moves from (2,2) to (3,2). white : Pawn moves from (7,2) to (8,2). black : King moves from (3,2) to (4,2). white : Pawn moves from (8,2) to (9,2). black : King moves from (4,2) to (5,2). white : Pawn moves from (9,2) to (10,2). white Pawn has reached the topmost row (nth row), so, white will convert it into a Queen. Black King cannot eliminate this Queen as it is too far. So, finally, White Wins.
'''

t = int(input())
for _ in range(t):
    n, a, b, c, d, Move = map(int, input().split())
    bk = (c, d)
    wp = (a, b)
    wk = (1, n)

    def cango(u, v):
        return {(u + 1, v), (u - 1, v), (u, v + 1), (u, v - 1), (u + 1, v + 1), (u + 1, v - 1), (u - 1, v + 1), (u - 1, v - 1)}


    while True:
        if Move == 0:
            # print("\n...White's move...")
            # print(f"White's pawn is at {wp}")
            # print(f"Black's king is at {bk}")
            # print(f"White's king is at {wk}")
            if wp[0] == n:
                print("White Wins")
                break
            else:
                if (wp[0] + 1, wp[1]) == bk:
                    if bk in cango(wk[0], wk[1]):
                        print("White Wins")
                        break
                    else:
                        wk = (wk[0]+1, bk[1]-1)
                else:
                    wp = (wp[0] + 1, wp[1])
        else:
            # print("\n...Black's move...")
            # print(f"White's pawn is at {wp}")
            # print(f"Black's king is at {bk}")
            # print(f"White's king is at {wk}")
            if wp in cango(bk[0], bk[1]):
                print("Draw")
                break
            else:
                if wp[0] > bk[0] and wp[1] > bk[1]:
                    bk = (bk[0] + 1, bk[1] + 1)
                elif wp[0] < bk[0] and wp[1] < bk[1]:
                    bk = (bk[0] - 1, bk[1] - 1)
                elif wp[0] < bk[0] and wp[1] > bk[1]:
                    bk = (bk[0] - 1, bk[1] + 1)
                elif wp[0] > bk[0] and wp[1] < bk[1]:
                    bk = (bk[0] + 1, bk[1] - 1)
        Move = not Move