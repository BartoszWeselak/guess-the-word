import player as play
import word as wrd

class game:

    def __init__(self,word):
        self.anwser=word
        self.word=word.upper()
        self.word=[x for x in self.word]
        self.guessed_words=[]
        self.score=0
        print(self.anwser)
    def check_letter(self,char,player):
        print(f"debug {char}")
        char = char.upper()
        if char in self.guessed_words:
            print("word already guessed")
        else:
            if char in self.word:
                self.guessed_words.append(char)
                self.score+=1
                return "right anwser"
            elif player.get_life()>0:
                self.life_loss(player)
                return "wrong anwser"
            else:
                print("game over")
                print(f"your score is {self.score}")
                return "wrong anwser"

    def __str__(self):
        return self.word

    def show_anwsered(self):
        return self.guessed_words

    def life_loss(self,player):
        player.wrong_anwser(life_loss=1)

    def get_score(self):
        return self.score

    def set_score(self,score):
        self.score=score

    def get_anwser(self):
        return self.anwser

    def get_word(self):
        return self.word

    def restart_guessed_words(self):
        self.guessed_words = []

    def set_new_word(self,word):
        self.anwser = word
        self.word = word.upper()
        self.word = [x for x in self.word]
        self.guessed_words = []
