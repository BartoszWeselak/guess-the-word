import word_generator as word
import player as play
import gui
if __name__ == "__main__":
    game = word.game("xd")
    print(game.__str__())
    print(game.check_letter("x"))
    print(game.check_letter("d"))
    print(game.check_letter("c"))

    print(game.show_anwsered())
    # gui.main_window()
    new_player=play.player("Arek")
    new_player.wrong_anwser()
    print(new_player.get_life())