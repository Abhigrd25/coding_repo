import tkinter as tk
import random
import time

class WhackAMole:
    def __init__(self, master):
        self.master = master
        self.master.title("Whack-a-Mole")
        self.score = 0
        self.time_left = 30 
        self.mole_position = None

       
        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=('Arial', 16))
        self.score_label.grid(row=0, column=0, columnspan=3)

       
        self.time_label = tk.Label(master, text=f"Time left: {self.time_left}s", font=('Arial', 16))
        self.time_label.grid(row=0, column=3, columnspan=3)

       
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text='', font=('Arial', 20), width=6, height=3, command=lambda row=i, col=j: self.hit_mole(row, col))
                button.grid(row=i+1, column=j, padx=10, pady=10)
                row.append(button)
            self.buttons.append(row)

       
        self.update_timer()
        self.show_mole()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}s")
            self.master.after(1000, self.update_timer)  
        else:
            self.end_game()

    def show_mole(self):
        if self.time_left > 0:
            if self.mole_position:
                self.buttons[self.mole_position[0]][self.mole_position[1]].config(text='')  

           
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            self.mole_position = (row, col)
            self.buttons[row][col].config(text='Mole')

           
            self.master.after(800, self.show_mole)

    def hit_mole(self, row, col):
        if self.mole_position == (row, col):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.buttons[row][col].config(text='') 
            self.mole_position = None

    def end_game(self):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled') 
        tk.messagebox.showinfo("Game Over", f"Time's up! Your final score is {self.score}.")

if __name__ == "__main__":
    root = tk.Tk()
    game = WhackAMole(root)
    root.mainloop()
