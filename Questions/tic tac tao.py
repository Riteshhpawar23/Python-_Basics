import tkinter as tk
from tkinter import messagebox
import random

# Global Variables
PLAYER = None
AI = None
board = [['' for _ in range(3)] for _ in range(3)]

# Check for a winner and return winning positions
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0], [(i, 0), (i, 1), (i, 2)]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i], [(0, i), (1, i), (2, i)]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    if all(board[r][c] != '' for r in range(3) for c in range(3)):
        return 'Tie', []
    return None, []

# Highlight winning combination
def highlight_winner(positions):
    for r, c in positions:
        buttons[r][c].config(bg='#ff073a')

# Minimax algorithm for AI
def minimax(is_maximizing):
    winner, _ = check_winner()
    if winner == PLAYER:
        return -1
    elif winner == AI:
        return 1
    elif winner == 'Tie':
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = AI
                    score = minimax(False)
                    board[r][c] = ''
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = PLAYER
                    score = minimax(True)
                    board[r][c] = ''
                    best_score = min(best_score, score)
        return best_score

# AI move
def ai_move():
    status_label.config(text="AI is thinking...")
    root.update()
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = AI
                score = minimax(False)
                board[r][c] = ''
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    if best_move:
        board[best_move[0]][best_move[1]] = AI
        buttons[best_move[0]][best_move[1]].config(text=AI, state=tk.DISABLED, disabledforeground='#ff073a')
        status_label.config(text="Your turn")
        check_game_over()

# Check game over state
def check_game_over():
    winner, positions = check_winner()
    if winner:
        if winner == 'Tie':
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            highlight_winner(positions)
            messagebox.showinfo("Game Over", f"{winner} Wins!")
        root.quit()

# Handle player move
def player_move(r, c):
    if board[r][c] == '':
        board[r][c] = PLAYER
        buttons[r][c].config(text=PLAYER, state=tk.DISABLED, disabledforeground='#39ff14')
        check_game_over()
        if not check_winner()[0]:
            ai_move()

# Player selection
def choose_symbol(symbol):
    global PLAYER, AI
    PLAYER = symbol
    AI = 'O' if PLAYER == 'X' else 'X'
    selection_frame.destroy()

# Initialize GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#000000")

selection_frame = tk.Frame(root, bg="#000000")
selection_frame.pack(pady=20)
selection_label = tk.Label(selection_frame, text="Choose X or O", font=('Arial', 18), bg="#000000", fg="#39ff14")
selection_label.pack()
btn_x = tk.Button(selection_frame, text='X', font=('Arial', 18), command=lambda: choose_symbol('X'), bg="#0d0d0d", fg="#39ff14")
btn_x.pack(side=tk.LEFT, padx=10)
btn_o = tk.Button(selection_frame, text='O', font=('Arial', 18), command=lambda: choose_symbol('O'), bg="#0d0d0d", fg="#ff073a")
btn_o.pack(side=tk.RIGHT, padx=10)

frame = tk.Frame(root, bg="#000000")
frame.pack(side=tk.LEFT, padx=20, pady=20)

buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(frame, text='', font=('Arial', 24), width=5, height=2,
                                  command=lambda r=r, c=c: player_move(r, c),
                                  bg="#0d0d0d", fg="#39ff14", activebackground="#ff073a", relief=tk.RAISED, borderwidth=3)
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

status_frame = tk.Frame(root, bg="#000000")
status_frame.pack(side=tk.RIGHT, padx=20, pady=20)
status_label = tk.Label(status_frame, text="Your turn", font=('Arial', 18), bg="#000000", fg="#39ff14")
status_label.pack()

root.mainloop()
