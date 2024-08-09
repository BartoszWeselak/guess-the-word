import player as play

words = [
    "testtest","test"
]

class game:

    def __init__(self,word):
        self.word=word
        self.word=[x for x in self.word]
        self.guessed_words=[]
    def check_letter(self,char,player):
        if char in self.word:
            self.guessed_words.append(char)
            return "right anwser"
        elif player.get_life()>0:
            self.life_loss(player)
            return "wrong anwser"
        else:
            print("game over")
            return "wrong anwser"

    def __str__(self):
        return self.word

    def show_anwsered(self):
        return self.guessed_words

    def life_loss(self,player):
        player.wrong_anwser(life_loss=1)

