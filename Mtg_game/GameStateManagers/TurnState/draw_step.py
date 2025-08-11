from Mtg_game.player import Player
class DrawStep:
    
    def execute(self, player):
        player.draw_card()