import tkinter as tk


def main_window():
    root = tk.Tk()
    root.title("Guess")
    root.geometry("300x700")
    root.configure(bg='lightblue')
    game_window(root)
    root.mainloop()


def game_window(root):
    label = tk.Label(root, text="Guess the word", font=("Helvetica", 16), bg='lightblue')
    label.pack()
    word_label = tk.Label(root, text="_ _ _ _", font=("Helvetica", 24), bg='lightblue')
    word_label.pack(pady=20)

    keyboard_frame = tk.Frame(root, bg='lightblue')
    keyboard_frame.pack(pady=20)

    create_keyboard(keyboard_frame)

def create_keyboard(frame):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(letters):
        button = tk.Button(frame, text=letter, command=lambda l=letter: submit_letter(l), width=4, height=2, font=("Helvetica", 14))
        button.grid(row=i//7, column=i%7, padx=5, pady=5)

def keyboard():
    print("debug")
def submit_letter(letter):
    print(letter)
