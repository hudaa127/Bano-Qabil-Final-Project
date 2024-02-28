# Team Members : Noor Ul Huda (Team Leader), Shumaila Basit
# Tic Tac Toe
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=3,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.toggle_player()

    def check_winner(self):
        for i in range(3):
            if (self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != ""
                    or self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != ""):
                return True
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != ""
                or self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != ""):
            return True
        return False

    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
