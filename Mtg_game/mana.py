from card import Card 

class Mana(Card):
    
    def __init__(self, name, mana_cost, card_type, mana_type):
        super().__init__(self, name, mana_cost, card_type)
        self.blue = False
        self.red = False
        self.green = False 
        self.white = False 
        self.black = False 
        self.mana_type = mana_type.lower()
            
        

