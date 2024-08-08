import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result_text = f"Player: {player_choice}\nComputer: {computer_choice}\n"

    if player_choice == computer_choice:
        result_text += "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_text += "You win!"
    else:
        result_text += "Computer wins!"
    
    messagebox.showinfo("Result", result_text)


window = tk.Tk()
window.title("Rock-Paper-Scissors")


heading_label = tk.Label(window, text="Rock-Paper-Scissors", font=('Arial', 18))
heading_label.pack(pady=10)


instructions_label = tk.Label(window, text="Choose one:", font=('Arial', 12))
instructions_label.pack(pady=5)


rock_button = tk.Button(window, text="Rock", width=10, height=2, font=('Arial', 14),
                        command=lambda: determine_winner("Rock"))
rock_button.pack(pady=5)


paper_button = tk.Button(window, text="Paper", width=10, height=2, font=('Arial', 14),
                         command=lambda: determine_winner("Paper"))
paper_button.pack(pady=5)


scissors_button = tk.Button(window, text="Scissors", width=10, height=2, font=('Arial', 14),
                            command=lambda: determine_winner("Scissors"))
scissors_button.pack(pady=5)


window.mainloop()
