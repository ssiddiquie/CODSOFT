import tkinter as tk
import math
import random

def play_round(user_choice):
    global wins, ties, defeats, turns
    possible = ["Rock", "Paper", "Scissors"]
    bot_choice = random.choice(possible)

    result_label.config(text=f"Bot chose: {bot_choice.lower()}")

    if user_choice == bot_choice:
        outcome_label.config(text="It's a tie!")
        ties += 1
    elif (user_choice == "Paper" and bot_choice == "Rock") or \
         (user_choice == "Rock" and bot_choice == "Scissors") or \
         (user_choice == "Scissors" and bot_choice == "Paper"):
        outcome_label.config(text="You won!")
        wins += 1
    else:
        outcome_label.config(text="You lost!")
        defeats += 1

    turns += 1
    turns_label.config(text=f"Turns: {turns}")
    wins_label.config(text=f"Wins: {wins}")
    ties_label.config(text=f"Ties: {ties}")
    defeats_label.config(text=f"Defeats: {defeats}")

app = tk.Tk()
app.title("Rock, Paper, Scissors Game")

wins = 0
ties = 0
defeats = 0
turns = 0

instructions_label = tk.Label(app, text="Choose Rock, Paper, or Scissors:")
instructions_label.pack()

rock_button = tk.Button(app, text="Rock", command=lambda: play_round("Rock"))
rock_button.pack()

paper_button = tk.Button(app, text="Paper", command=lambda: play_round("Paper"))
paper_button.pack()

scissors_button = tk.Button(app, text="Scissors", command=lambda: play_round("Scissors"))
scissors_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

outcome_label = tk.Label(app, text="")
outcome_label.pack()

wins_label = tk.Label(app, text=f"Wins: {wins}")
wins_label.pack()

ties_label = tk.Label(app, text=f"Ties: {ties}")
ties_label.pack()

defeats_label = tk.Label(app, text=f"Defeats: {defeats}")
defeats_label.pack()

turns_label = tk.Label(app, text=f"Turns: {turns}")
turns_label.pack()

app.mainloop()
