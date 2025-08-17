from GameStateManagers.turn_manager import TurnManager


class GameManager:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn_count = 1
        self.current_attacker = player1
        self.current_defender = player2
        self.game_over = False
        self.winner = None
    
    def check_win_condition(self):
        """Check if game is over and set winner"""
        if self.player1.life <= 0:
            self.game_over = True
            self.winner = self.player2
            return True
        elif self.player2.life <= 0:
            self.game_over = True
            self.winner = self.player1
            return True
        return False
    
    def end_turn(self):
        """Handle end of turn effects"""
        print(f"\n--- End of {self.current_attacker.name}'s Turn ---")
        
        # Untap all creatures
        self.current_attacker.untap_all_creatures()
        self.current_defender.untap_all_creatures()
        
        # Heal all damage at end of turn
        for creature in self.current_attacker.creatures + self.current_defender.creatures:
            if hasattr(creature, 'heal_all_damage'):
                creature.heal_all_damage()
        
        print(f"Game State: {self.player1} | {self.player2}")
        
        # Switch turns
        self.current_attacker, self.current_defender = self.current_defender, self.current_attacker
        self.turn_count += 1
    
    def run_turn(self):
        """Run a single turn"""
        print(f"\n{'='*50}")
        print(f"TURN {self.turn_count} - {self.current_attacker.name}'s Attack Phase")
        print(f"{'='*50}")
        
        # Create combat manager and run combat
        combat = CombatManager(self.current_attacker, self.current_defender)
        combat.run_combat()
        
        # Check for game over
        if self.check_win_condition():
            return
        
        # End turn
        self.end_turn()
    
    def should_continue(self):
        """Ask player if they want to continue the game"""
        try:
            continue_game = input("\nPress Enter to continue to next turn, or 'q' to quit: ").strip().lower()
            return continue_game != 'q'
        except KeyboardInterrupt:
            print("\nGame ended.")
            return False
    
    def run_game(self):
        """Run the complete game loop"""
        print(f"=== MAGIC: THE GATHERING GAME ===")
        print(f"{self.player1}")
        print(f"{self.player2}")
        
        while not self.game_over:
            self.run_turn()
            
            if self.game_over:
                break
                
            if not self.should_continue():
                print("Game ended by player choice.")
                break
        
        self.display_final_results()
    
    def display_final_results(self):
        """Display final game state and winner"""
        if self.winner:
            print(f"\n🎉 {self.winner.name} WINS! {self.get_loser().name} is defeated!")
        
        print(f"\n=== FINAL GAME STATE ===")
        print(f"{self.player1}")
        print(f"{self.player2}")
        print("Thanks for playing Magic: The Gathering!")
    
    def get_loser(self):
        """Get the losing player"""
        return self.player2 if self.winner == self.player1 else self.player1