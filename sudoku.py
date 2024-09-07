import tkinter as tk
from tkinter import messagebox
import random

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=4, font=('Arial', 18), justify='center', bd=2, relief='solid')
                entry.grid(row=i, column=j, padx=1, pady=1, sticky='nsew')

                self.root.grid_rowconfigure(i, weight=1)
                self.root.grid_columnconfigure(j, weight=1)
                
                self.entries[i][j] = entry


        check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=9, pady=10)

        self.fill_grid()

    def fill_grid(self):

        base_grid = self.generate_sudoku_grid()

        for i in range(9):
            for j in range(9):
                if base_grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(base_grid[i][j]))
                    self.entries[i][j].config(state='readonly')

    def generate_sudoku_grid(self):

        base_grid = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if random.random() < 0.4:  #40% de rpobabilidad de aparicion
                    num = random.randint(1, 9)
                    if self.is_valid_number(base_grid, i, j, num):
                        base_grid[i][j] = num

        return base_grid

    def is_valid_number(self, grid, row, col, num):

        if num in grid[row]:
            return False
        if num in (grid[i][col] for i in range(9)):
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False

        return True

    def check_solution(self):
        solution = [[self.entries[i][j].get() for j in range(9)] for i in range(9)]
        if self.is_valid_solution(solution):
            messagebox.showinfo("Sudoku", "Solution is correct!")
        else:
            messagebox.showerror("Sudoku", "Solution is incorrect.")

    def is_valid_solution(self, grid):
        try:
            grid = [[int(grid[i][j]) for j in range(9)] for i in range(9)]
        except ValueError:
            return False

        for i in range(9):
            if len(set(grid[i])) != 9:
                return False
            if len(set(row[i] for row in grid)) != 9:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if len(set(subgrid)) != 9:
                    return False

        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()