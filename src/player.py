
class player:
    def __init__(self,name):
        self.name=name
        self.life=3

    def show_player_name(self):
        return self.name

    def wrong_anwser(self,life_loss):
        self.life-=life_loss
    def get_life(self):
        return self.life
    def get_score(self):
        return self.score

    def set_score(self,score):
        self.score=score

