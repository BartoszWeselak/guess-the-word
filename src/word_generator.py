import player as play

words = [
    "testtest","test"
]

class game:

    def __init__(self,word):
        self.word=word
        self.word=[x for x in self.word]
        self.guessed_words=[]
    def check_letter(self,char):
        if char in self.word:
            self.guessed_words.append(char)
        else:
            return "wrong anwser"
    def __str__(self):
        return self.word

    def show_anwsered(self):
        return self.guessed_words

    def life_loss(self,player):
        pla
