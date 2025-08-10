from creature import Creature
from player import Player 
from combat_manager import CombatManager

def main():
    # Create players
    player1 = Player("Alice")
    player2 = Player("Bob")
    
    # Give players creatures
    player1.add_creature(Creature("Red Dragon", 6, 5, 5,["flying"]))
    player1.add_creature(Creature("Goblin Warrior", 2, 2, 1, ["flying"]))
    player1.add_creature(Creature("Lightning Elemental", 3, 4, 1,[]))
    
    player2.add_creature(Creature("White Knight", 3, 2, 3,[]))
    player2.add_creature(Creature("Wall of Stone", 2, 0, 7, []))
    player2.add_creature(Creature("Guardian Angel", 5, 3, 4, ["flying"]))
    
    # Remove summoning sickness for demo
    player1.untap_all_creatures()
    player2.untap_all_creatures()
    
    print(f"=== MAGIC: THE GATHERING GAME ===")
    print(f"{player1}")
    print(f"{player2}")
    
    turn_count = 1
    current_attacker = player1
    current_defender = player2
    
    # Game loop
    while player1.life > 0 and player2.life > 0:
        print(f"\n{'='*50}")
        print(f"TURN {turn_count} - {current_attacker.name}'s Attack Phase")
        print(f"{'='*50}")
        
        # Check if attacker has creatures that can attack
        if not current_attacker.get_available_attackers():
            print(f"{current_attacker.name} has no creatures that can attack!")
            print("Skipping combat phase...")
        else:
            # Create combat manager for this turn
            combat = CombatManager(current_attacker, current_defender)
            
            # Combat phases
            combat.declare_attackers()
            
            # Only do blocking if there are attackers
            if combat.attackers:
                combat.declare_blockers()
                combat.resolve_combat()
            else:
                print("No attackers declared, skipping combat.")
        
        # Check for game over
        if player1.life <= 0:
            print(f"\n🎉 {player2.name} WINS! {player1.name} is defeated!")
            break
        elif player2.life <= 0:
            print(f"\n🎉 {player1.name} WINS! {player2.name} is defeated!")
            break
        
        # End of turn - untap creatures and heal damage
        print(f"\n--- End of {current_attacker.name}'s Turn ---")
        current_attacker.untap_all_creatures()
        current_defender.untap_all_creatures()
        
        # Heal all damage at end of turn
        for creature in current_attacker.creatures + current_defender.creatures:
            if hasattr(creature, 'heal_all_damage'):
                creature.heal_all_damage()
        
        print(f"Game State: {player1} | {player2}")
        
        # Switch turns
        current_attacker, current_defender = current_defender, current_attacker
        turn_count += 1
        
        # Ask if players want to continue or quit
        try:
            continue_game = input("\nPress Enter to continue to next turn, or 'q' to quit: ").strip().lower()
            if continue_game == 'q':
                print("Game ended by player choice.")
                break
        except KeyboardInterrupt:
            print("\nGame ended.")
            break
    
    print(f"\n=== FINAL GAME STATE ===")
    print(f"{player1}")
    print(f"{player2}")
    print("Thanks for playing Magic: The Gathering!")

if __name__ == "__main__":
    main()