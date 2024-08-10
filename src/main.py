import game
import player as play
import gui
import word
words = [
    "butterfly",
    "mountain",
    "astronomy",
    "puzzle",
    "elephant",
    "umbrella",
    "computer",
    "library",
    "mystery",
    "sunshine",
    "penguin",
    "airplane",
    "bicycle",
    "fireworks",
    "jellyfish",
    "volcano",
    "rainbow",
    "sandcastle",
    "skeleton",
    "spaceship"
]

if __name__ == "__main__":
    game = game.game(word.pick_word(words))
    new_player=play.player("Arek")
    gui.main_window(game,new_player)

