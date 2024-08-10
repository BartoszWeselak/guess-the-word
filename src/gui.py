import tkinter as tk
import game
import player as play
import word
import random

def main_window(game,play):
    game = game.game(word.pick_word())

    root = tk.Tk()
    root.title("Guess")
    root.geometry("600x500")
    root.configure(bg='lightblue')
    restart_button(root,game,play)

    root.mainloop()

def restart_button(root,game,play):

    start_button = tk.Button(root, width=20, padx=2, pady=2, font=('Helvetica', 12), bg='lightgreen', fg='white',
                             text="Start new game", command=lambda: start_game(root, game, play,start_button))
    start_button.pack()


def start_game(root,game,play,start_button):
    game.restart_guessed_words()

    for widget in root.winfo_children():
        widget.destroy()

    game_window(root,game,play)

def game_window(root,game,play):
    spacer(root,1)

    label = tk.Label(root, text="Guess the word", font=("Helvetica", 16), bg='lightblue')
    label.pack()
    stats = display_stats(root, game, play)
    stats_label = tk.Label(root, text=stats, font=("Helvetica", 16), bg='lightblue')
    stats_label.pack()
    text=display_word(game)
    word_label = tk.Label(root, text=text, font=("Helvetica", 24), bg='lightblue')
    word_label.pack(pady=20)

    keyboard_frame = tk.Frame(root, bg='lightblue')
    keyboard_frame.pack(pady=20)

    create_keyboard(root,keyboard_frame,game,play,word_label,stats_label)


def display_word(game):
    text = ""
    for w in game.__str__():
        if w in game.show_anwsered():
            text += " "+w+" "
        else:
            text += " _ "
    return text
def create_keyboard(root,frame,game,play,word_label,stats_label):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(letters):
        button = tk.Button(frame, text=letter, command=lambda l=letter: submit_letter(root,l,game,play,word_label,stats_label), width=4, height=2, font=("Helvetica", 14))
        button.grid(row=i//7, column=i%7, padx=5, pady=5)


def submit_letter(root,letter,game,play,word_label,stats_label):
    game.check_letter(letter,play)

    if play.get_life() ==0:
        game_over(root,game,play)
    else:
        stats=display_stats(root,game,play)
        stats_label.config(text=stats)
        text=display_word(game)
        word_label.config(text=text)
        if game.get_word() == game.show_anwsered():
            print(game.get_word())

def game_over(root,game,play):
    for widget in root.winfo_children():
        widget.destroy()
    score = game.get_score()
    play.set_life(3)
    spacer(root,6)

    label = tk.Label(root, text="Game Over", font=("Helvetica", 16), bg='lightblue')
    label.pack()
    correct_label = tk.Label(root, text=f"correct word is {game.get_anwser()}", font=("Helvetica", 16), bg='lightblue')
    correct_label.pack()
    label_score = tk.Label(root, text=f"Your score is {score}", font=("Helvetica", 16), bg='lightblue')
    label_score.pack()
    game.set_score(0)
    restart_button(root, game, play)


def spacer(root,n=1):
    for i in range(n):
        space = tk.Label(root, text="", font=("Helvetica", 8), bg='lightblue')
        space.pack()

def display_stats(root,game,play):
    hearth_icon = "\u2764"
    hearts=""
    score=game.get_score()
    for i in range(play.get_life()):
        hearts+=hearth_icon
    stats=f"Life: {hearts} Score: {score}"

    return stats