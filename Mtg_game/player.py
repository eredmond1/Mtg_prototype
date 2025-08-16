import random
from Mtg_game.Cards.card import Card  # If you need to check card types
from Mtg_game.Cards.creature import Creature 

class Player:
    def __init__(self, name, starting_life=20):
        self.name = name
        self.life = starting_life
        self.creatures = []
        self.hand = []
        #red blue green white black 
        self.mana = [0,0,0,0,0]
        self.tapped_mana = [0,0,0,0,0]
        self.deck = []
        self.active_cards = []
        self.graveyard = []
        self.exile = []
    
    def add_creature(self, creature):
        """Add a creature to this player's battlefield"""
        self.creatures.append(creature)
        print(f"{self.name} controls {creature.name}")
    
    def get_available_attackers(self):
        """Get all creatures that can attack"""
        return [c for c in self.creatures if c.can_attack()]
    
    def get_available_blockers(self):
        """Get all creatures that can block"""
        return [c for c in self.creatures if c.can_block()]
    
    def add_to_hand(self, card):
        self.hand.append(card)
        
    def shuffle_deck(self):
        self.deck = random.shuffle(self.deck)
        
    def add_to_mana(self, card):
        match card.mana_type:
            case "red": self.mana[0] += 1
            case "blue": self.mana[1] += 1
            case "green": self.mana[2] +=1
            case "white": self.mana[3] += 1
            case "black": self.mana[4] += 1        
        
            

    def draw_card(self):
        if self.deck:
            new_card = self.deck.pop(0)
            self.hand.append(new_card)
        else:
            print(f"{self.name} has no cards left to draw!")
    
    def take_damage(self, damage):
        """Player takes damage"""
        self.life -= damage
        print(f"{self.name} takes {damage} damage! (Life: {self.life})")
        
        if self.life <= 0:
            print(f"{self.name} is defeated!")
            return True  # Player is dead
        return False
    
    def remove_creature(self, creature):
        """Remove a destroyed creature"""
        if creature in self.creatures:
            self.creatures.remove(creature)
            print(f"{creature.name} removed from {self.name}'s battlefield")
    
    def untap_all_creatures(self):
        """Untap all creatures at start of turn"""
        for creature in self.creatures:
            creature.untap()
            creature.resolve_summoning_sickness()
            
    def untap_all_mana(self):
        for i in range(len(self.mana)):
            self.mana[i] += self.tapped_mana[i]
            self.tapped_mana[i] = 0
    
    def __str__(self):
        return f"{self.name} (Life: {self.life}, Creatures: {len(self.creatures)})"
    
    def print_hand(self):
        print(f"\n{self.name}'s hand\n")
        if not self.hand:
            print("\nYou have no cards to play\n")
        else:
            for i, card in enumerate(self.hand, 1):
                print(f"{i}. {card}")
                
    def get_hand_count(self):
        return len(self.hand)
    
    def mana_check(self, card):
        card_mana = card.get_mana_cost()
        enough_mana = all(player_mana_color >= card_mana_color for player_mana_color, card_mana_color in zip(self.mana, card_mana))
        return enough_mana
    
    def take_mana(self, card):
        card_mana = card.get_mana_cost()
        for i in range(len(self.mana)):
            self.mana[i] -= card_mana[i]
            self.tapped_mana[i] += card_mana[i] 
            
            
    def play_card(self, card_num):
        card_num -= 1
        card = self.hand[card_num]
        match card.get_card_type():
            #you can handle this later
            case "mana": self.add_to_mana(card)
            case "creature":
                if self.mana_check(card):
                    self.take_mana(card)
                    del self.hand[card_num]
                    self.active_cards.append(card)
                    return True
                else:
                    return False
            
        
        
        
        