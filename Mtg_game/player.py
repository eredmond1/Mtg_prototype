

class Player:
    def __init__(self, name, starting_life=20):
        self.name = name
        self.life = starting_life
        self.creatures = []
        self.hand = []
        self.mana = 0
    
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
    
    def __str__(self):
        return f"{self.name} (Life: {self.life}, Creatures: {len(self.creatures)})"
