import random

class Sudoku:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]
        self.generate_board()
        self.create_puzzle()

    def generate_board(self):
        base = list(range(1, 10))
        random.shuffle(base)
        self.grid[0] = base

        for i in range(1, 9):
            self.grid[i] = self.grid[i - 1][3:] + self.grid[i - 1][:3]
            if i % 3 == 0:
                self.grid[i] = self.grid[i][1:] + [self.grid[i][0]]

    def create_puzzle(self):
        for _ in range(20):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0

    def check_win(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True

    def is_valid_move(self, row, col, value):
        for i in range(9):
            if self.grid[row][i] == value or self.grid[i][col] == value:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == value:
                    return False

        return True

    def make_move(self, row, col, value):
        if self.is_valid_move(row, col, value):
            self.grid[row][col] = value
            return True
        return False