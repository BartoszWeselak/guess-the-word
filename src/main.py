import word_generator as word
import player as play
import gui
if __name__ == "__main__":
    game = word.game("xd")
    new_player=play.player("Arek")
    new_player.wrong_anwser(1)


    print(game.show_anwsered())
    gui.main_window(game,new_player)

