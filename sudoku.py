import tkinter as tk
from sudoku_ui import SudokuUI
from sudoku_logic import Sudoku

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_game = Sudoku()
    sudoku_ui = SudokuUI(root, sudoku_game)
    root.mainloop()