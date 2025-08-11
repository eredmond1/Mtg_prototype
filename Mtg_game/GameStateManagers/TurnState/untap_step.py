from Mtg_game.player import Player 
class UntapStep:
    
    def execute(self, player):
        print(f"\n--- {player.name}'s Untap Phase --- \n")
        player.untap_all_creatures()
        player.untap_all_creatures()
        
        print("All permanents untapped, mana pool refreshed \n")