def sudoku(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                choices = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                for num in puzzle[i]:
                    choices.discard(num)
                for i in range(len(puzzle)):
                    choices.discard(puzzle[i][j])
                choices = list(choices)
                for choice in choices:
                    
