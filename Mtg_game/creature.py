from card import Card 

class Creature(Card):
    
    def __init__(self, name, mana_cost, power, toughness, abilities):
        
        if power < 0:
            raise ValueError("Power cannot be negative")
        if toughness <= 0:
            raise ValueError("Toughness must be greater than 0")
        if mana_cost < 0:
            raise ValueError("Mana cost cannot be negative")
        card_type = "Creature"
        super().__init__(name, mana_cost, card_type)
        self.power = power
        self.toughness = toughness
        self.is_tapped = False
        self.current_toughness = toughness
        # Dictionary to store +X/+X counters: {power_bonus: count}
        self.counters = {}
        #not implemented 
        self.flying = False
        #not implemented
        self.haste = False
        #not implemented
        self.vigilance = False
        #not implemented 
        self.first_turn = True
        
        # Initialize abilities
        self.init_abilities(abilities)
        
        
    def __str__(self):
        current_power = self.get_power()
        if self.counters:
            return f"{super().__str__()} [{current_power}/{self.current_toughness}] (Base: {self.power}/{self.toughness})"
        else:
            return f"{super().__str__()} [{current_power}/{self.current_toughness}]"
        
    def init_abilities(self, abilities):
        if len(abilities) < 1:
            return 
        
        for i in range(len(abilities)):
            ability = abilities[i].lower()
            match ability:
                case "flying":
                    self.flying = True
                    
                case "haste":
                    self.haste = True
                    
                case "vigilance":
                    self.vigilance = True
        return
    
    def tap(self):
        self.is_tapped = True
    
    def untap(self):
        self.is_tapped = False
        
    def can_attack(self):
        return not (self.summoning_sickness or self.is_tapped) and self.current_toughness > 0
    
    def can_block(self):
        return not self.is_tapped and self.current_toughness > 0
    
    def get_power(self):
        """Get current power including counters"""
        if not self.counters:
            return self.power
        
        counter_power = 0
        for power_bonus, count in self.counters.items():
            counter_power += power_bonus * count
        return self.power + counter_power
    
    def add_counter(self, power_bonus):
        """Add a +X/+X counter to the creature"""
        if power_bonus in self.counters:
            self.counters[power_bonus] += 1
        else:
            self.counters[power_bonus] = 1
        
        # Increase current toughness for the toughness boost
        self.current_toughness += power_bonus
        print(f"{self.name} gets a +{power_bonus}/+{power_bonus} counter!")
    
    def remove_counter(self, power_bonus):
        """Remove a +X/+X counter from the creature"""
        if power_bonus in self.counters and self.counters[power_bonus] > 0:
            self.counters[power_bonus] -= 1
            
            # Decrease current toughness
            self.current_toughness -= power_bonus
            
            if self.counters[power_bonus] == 0:
                del self.counters[power_bonus]
                
            print(f"{self.name} loses a +{power_bonus}/+{power_bonus} counter!")
            return True
        return False
            
            
    
        
    def resolve_summoning_sickness(self):
        self.summoning_sickness = False
    
    def take_damage(self, damage):
        self.current_toughness -= damage
        print(f"{self.name} takes {damage} damage! ({self.current_toughness}/{self.toughness})")
        return self.current_toughness <= 0  # Returns True if creature dies