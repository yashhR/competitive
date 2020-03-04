class Sudoku(object):
    def __init__(self, data):
        self.sudoku = data

    def is_valid(self):
        columns = {}
        rows = {}
        for i in range(len(self.sudoku)):
            column = []
            for j in range(len(self.sudoku)):
                column.append(self.sudoku[j][i])
            rows[i + 1] = self.sudoku[i]
            columns[i+1] = column
        flag = None
        for i in range(len(self.sudoku)):
            x = columns[i+1].count(self.sudoku[i][i])
            y = rows[i+1].count(self.sudoku[i][i])
            if x == 1 and y == 1:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            return True
        else:
            return False

s = Sudoku([[1,4, 2,3],
           [3,2, 4,1],
           [4,1, 3,2],
           [2,3, 1,4]])
print(s.is_valid())



