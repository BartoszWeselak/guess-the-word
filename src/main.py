import game
import player as play
import gui

words = [
    "testtest","test"
]

if __name__ == "__main__":
    game = game.game(words[0])
    new_player=play.player("Arek")
    gui.main_window(game,new_player)

