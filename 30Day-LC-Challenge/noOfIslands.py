class Solution:
    def numIslands(grid):
        def dfs(row, col):
            grid[row][col] = '-1'

            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == '1':
                    dfs(r, c)

        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islandCount += 1
                    dfs(row, col)
        return islandCount