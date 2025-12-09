from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("WELCOME TO ALL")
window.geometry("500x400")
window.config(bg="#E6F7FF")

# Title Label
title_lbl = Label(window, text="🎯 Welcome to the Guessing Game 🎯", 
                  font=("Arial Rounded MT Bold", 16), 
                  bg="#E6F7FF", fg="#003366")
title_lbl.pack(pady=20)

# Frame for entries
frame = Frame(window, bg="#E6F7FF")
frame.pack(pady=10)

# --- Labels and Entries ---
Label(frame, text="First Name:", bg="#E6F7FF", font=("Arial", 12)).grid(column=0, row=0, padx=5, pady=5, sticky="e")
en1 = Entry(frame, font=("Arial", 12), width=20)
en1.grid(column=1, row=0, padx=5, pady=5)

Label(frame, text="Middle Name:", bg="#E6F7FF", font=("Arial", 12)).grid(column=0, row=1, padx=5, pady=5, sticky="e")
en2 = Entry(frame, font=("Arial", 12), width=20)
en2.grid(column=1, row=1, padx=5, pady=5)

Label(frame, text="Last Name:", bg="#E6F7FF", font=("Arial", 12)).grid(column=0, row=2, padx=5, pady=5, sticky="e")
en3 = Entry(frame, font=("Arial", 12), width=20)
en3.grid(column=1, row=2, padx=5, pady=5)

# --- Functions ---
def start_game():
    name = f"{en1.get()} {en2.get()} {en3.get()}".strip()
    if not en1.get() or not en3.get():
        messagebox.showwarning("Missing Info", "Please enter at least First and Last Name!")
        return
    
    secret_num = random.randint(1, 100)
    attempts = 0

    def check_guess():
        nonlocal attempts
        try:
            guess = int(guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid number between 1 and 100.")
            return
        attempts += 1

        if guess < secret_num:
            result_label.config(text="📉 Too low! Try again.", fg="red")
        elif guess > secret_num:
            result_label.config(text="📈 Too high! Try again.", fg="orange")
        else:
            messagebox.showinfo("🎉 Correct!", f"Great job, {name}!\nYou guessed it in {attempts} attempts!")
            guess_window.destroy()

    # --- Guessing Window ---
    guess_window = Toplevel(window)
    guess_window.title("Random Number Guessing")
    guess_window.geometry("400x300")
    guess_window.config(bg="#F9FBE7")

    Label(guess_window, text=f"Hello {name} 👋", bg="#F9FBE7", font=("Arial Rounded MT Bold", 14)).pack(pady=10)
    Label(guess_window, text="I'm thinking of a number between 1 and 100.", bg="#F9FBE7", font=("Arial", 12)).pack(pady=5)

    guess_entry = Entry(guess_window, font=("Arial", 12), width=10, justify="center")
    guess_entry.pack(pady=10)

    Button(guess_window, text="Check Guess", command=check_guess, bg="#82E0AA", fg="black",
           font=("Arial", 12), width=15, relief="ridge").pack(pady=10)

    result_label = Label(guess_window, text="", bg="#F9FBE7", font=("Arial", 12))
    result_label.pack(pady=5)

def reset_fields():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)

# --- Buttons ---
btn_frame = Frame(window, bg="#E6F7FF")
btn_frame.pack(pady=20)

Button(btn_frame, text="SUBMIT", command=start_game, bg="#A3E4D7", fg="black",
       font=("Arial", 12, "bold"), width=10, relief="raised", bd=3).grid(column=0, row=0, padx=10)

Button(btn_frame, text="RESET", command=reset_fields, bg="#F5B7B1", fg="black",
       font=("Arial", 12, "bold"), width=10, relief="raised", bd=3).grid(column=1, row=0, padx=10)

window.mainloop()
