'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


def solve(grid):
    for i in range(1, len(grid[0])):
        grid[0][i] = grid[0][i] + grid[0][i-1]
    for i in range(1, len(grid)):
        grid[i][0] = grid[i][0] + grid[i-1][0]
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] = grid[row][col] + min(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]


print(solve([
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]))

'''
The idea is the same as the no.of paths problem. (Either the staircase problem or the top-left to right-bottom problem)

Given the statement that we can only move right or down at any point(if it allows), we know that --
-- any point in the grid CAN BE REACHED either from the cell above or the cell to the left.

That is ground building block of the logic.

Also, it can be observed that the problem can be broken down into multiple subproblems, i.e., the minimum path from
top-left to any point in the grid.

SO, we will get the minimum path to all the cells in the grid and build on the basic logic that was specified above.


consider that we have a 2X2 grid 
[
[1, 2],
[3, 4]
]

We know that the only way to reach any of the cells in the first row is just by going right.
Similarly, the only way to reach any of the cells in the first column is just by going down.

So, the minimum path would be the the cost of that cell and the cost taken to reach the cell before it (left/above).


That makes the cost to reach 2 as 1+2 and the cost to reach 3 as 1+3

To reach 4, we have two ways, down-right or right-down-- now that we have the cost to reach 2 and 3,
we can decide which way to go by cost of 4 and the minimum of cost of the two ways,

4 + min(3, 4) = 7
cost to reach a cell = cost of the cell + min(cost to reach the cell to the left of the cell, cost to reach the cell above) 
'''