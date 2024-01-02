import tkinter as tk
from tkinter import messagebox
from sudoku_logic import Sudoku
import random

class SudokuUI:
    def __init__(self, root, sudoku):
        self.root = root
        self.root.title("Судоку")
        self.sudoku = sudoku
        self.colors = ["#FFEB3B", "#FF4081", "#4CAF50", "#03A9F4", "#FF9800", "#9C27B0"]
        random.shuffle(self.colors)
        self.buttons = []
        
        self.create_grid()
        
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.sudoku.grid[i][j]
                color = self.colors[(i * 9 + j) % 6]
                    
                if cell_value == 0:
                    button = tk.Button(self.root, text="", width=5, height=2, bg=color, fg="black", disabledforeground="black", command=lambda row=i, col=j: self.make_move(row, col))
                else:
                    button = tk.Button(self.root, text=str(cell_value), width=5, height=2, state=tk.DISABLED, bg=color, fg="black", disabledforeground="black")

                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)

        check_button = tk.Button(self.root, text="Перевірити", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=9, pady=10)

        restart_button = tk.Button(self.root, text="Перезапустити гру", command=self.restart_game)
        restart_button.grid(row=9, column=3, columnspan=3)

    def restart_game(self):
        self.generate_colors()
        self.sudoku = Sudoku()
        self.update_grid()

    def make_move(self, row, col):
        if self.sudoku.grid[row][col] == 0:
            entry_window = tk.Toplevel(self.root)
            entry_window.title("Введіть число")

            entry_label = tk.Label(entry_window, text="Введіть число (1-9):")
            entry_label.pack()

            entry_var = tk.StringVar()
            entry_entry = tk.Entry(entry_window, textvariable=entry_var, width=5)
            entry_entry.pack()

            entry_button = tk.Button(entry_window, text="Підтвердити", command=lambda: self.validate_move(row, col, entry_var.get(), entry_window))
            entry_button.pack()

    def validate_move(self, row, col, value, entry_window):
        try:
            value = int(value)
            if 1 <= value <= 9:
                if self.sudoku.make_move(row, col, value):
                    self.update_grid()
                    if self.sudoku.check_win():
                        messagebox.showinfo("Вітаємо!", "Ви виграли!")
                        self.restart_game()
                else:
                    messagebox.showerror("Помилка", "Це значення не підходить для клітинки.")
            else:
                messagebox.showerror("Помилка", "Будь ласка, введіть число від 1 до 9.")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть ціле число від 1 до 9.")

        entry_window.destroy()

    def update_grid(self):
        for i in range(81):
            cell_value = self.sudoku.grid[i // 9][i % 9]
            color = self.colors[i % 6]
            if cell_value == 0:
                self.buttons[i].configure(text="", bg=color) 
            else:
                self.buttons[i].configure(text=str(cell_value), state=tk.DISABLED, bg=color)

    def check_solution(self):
        if self.sudoku.check_win():
            messagebox.showinfo("Вітаємо!", "Ви вже виграли!")
        else:
            messagebox.showinfo("Помилка", "Ви ще не виграли. Продовжуйте гру!")
            
    def generate_colors(self):
        random.shuffle(self.colors)

    def generate_color(self):
        return random.choice(self.colors)