
class player:
    def __init__(self,name):
        self.name=name
        self.life=3
        self.score=0

    def show_player_name(self):
        return self.name

    def wrong_anwser(self):
        self.life-=1
    def get_life(self):
        return self.life