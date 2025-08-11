from Mtg_game.Cards.card import Card 

class Mana(Card):
    
    def __init__(self, name, mana_cost, card_type, mana_type):
        super().__init__(name, mana_cost, card_type)
        self.mana_type = mana_type.lower()



