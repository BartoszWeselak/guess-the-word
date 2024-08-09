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
    text=display_word(word)
    word_label = tk.Label(root, text=text, font=("Helvetica", 24), bg='lightblue')
    word_label.pack(pady=20)

    keyboard_frame = tk.Frame(root, bg='lightblue')
    keyboard_frame.pack(pady=20)

    create_keyboard(root,keyboard_frame,word,play,word_label)


def display_word(word):
    text = ""
    for w in word.__str__():
        if w in word.show_anwsered():
            text += " "+w+" "
        else:
            text += " _ "
    return text
def create_keyboard(root,frame,word,play,word_label):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(letters):
        button = tk.Button(frame, text=letter, command=lambda l=letter: submit_letter(root,l,word,play,word_label), width=4, height=2, font=("Helvetica", 14))
        button.grid(row=i//7, column=i%7, padx=5, pady=5)


def submit_letter(root,letter,word,play,word_label):
    word.check_letter(letter,play)
    if play.get_life() ==0:
        game_over(root,word)
    else:
        text=display_word(word)
        word_label.config(text=text)


def game_over(root,word):
    for widget in root.winfo_children():
        widget.destroy()
    score = word.get_score()
    label = tk.Label(root, text="Game Over", font=("Helvetica", 16), bg='lightblue')
    label.pack()
    label_score = tk.Label(root, text=f"Your score is {score}", font=("Helvetica", 16), bg='lightblue')
    label_score.pack()
