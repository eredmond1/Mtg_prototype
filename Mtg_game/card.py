class Card:
    
  
    def __init__(self, name, mana_cost, card_type):
        self.name = name 
        self.mana_cost = mana_cost
        self.card_type = card_type
        self.summoning_sickness = True
        
        
    def __str__(self):
        return f"{self.name} ({self.card_type}) - Cost: {self.mana_cost}"

    