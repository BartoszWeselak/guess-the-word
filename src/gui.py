import tkinter as tk
import word_generator as word
import player as play

def main_window(word,play):
    root = tk.Tk()
    root.title("Guess")
    root.geometry("600x500")
    root.configure(bg='lightblue')
    game_window(root,word,play)

    root.mainloop()


def game_window(root,word,play):
    label = tk.Label(root, text="Guess the word", font=("Helvetica", 16), bg='lightblue')
    label.pack()
    word_label = tk.Label(root, text="_ _ _ _", font=("Helvetica", 24), bg='lightblue')
    word_label.pack(pady=20)

    keyboard_frame = tk.Frame(root, bg='lightblue')
    keyboard_frame.pack(pady=20)

    create_keyboard(keyboard_frame,word,play)

def create_keyboard(frame,word,play):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(letters):
        button = tk.Button(frame, text=letter, command=lambda l=letter: submit_letter(l,word,play), width=4, height=2, font=("Helvetica", 14))
        button.grid(row=i//7, column=i%7, padx=5, pady=5)


def submit_letter(letter,word,play):
    word.check_letter(letter,play)
